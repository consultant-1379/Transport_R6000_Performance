# ********************************************************************
# Ericsson Inc.                                                 SCRIPT
# ********************************************************************
#
#
# (c) Ericsson Inc. 2022 - All rights reserved.
#
# The copyright to the computer program(s) herein is the property
# of Ericsson Inc. The programs may be used and/or copied only with
# the written permission from Ericsson Inc. or in accordance with the
# terms and conditions stipulated in the agreement/contract under
# which the program(s) have been supplied.
#
# ********************************************************************
# Name    :  ResetFiltersAndMarkings.py
# Date    :  13/03/2024
# Revision:  1.0
# Purpose :  Resets filters, markings, sliders, document properties to the default values when 'Reset All Markings and Filters' button clicked in the home page
#
# Usage   :  Transport Report
#

from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Application.Filters import *
from Spotfire.Dxp.Data import RowSelection,  IndexSet
from System.Collections.Generic import List,  Dictionary
from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Application import Filters as filters
from Spotfire.Dxp.Application.Filters import *
from Spotfire.Dxp.Application.Visuals import *

reset_pages_list = ['Node Level KPIs', 'Interface Level KPIs']


def reset_marking_and_filtering(): 
	
    for data_table in Document.Data.Tables: 
        for marking in Document.Data.Markings: 
            rows = RowSelection(IndexSet(data_table.RowCount,  False))
            marking.SetSelection(rows,  data_table)
                
        for filter_scheme in Document.FilteringSchemes: 
            filter_scheme.ResetAllFilters()


def reset_sliders(): 

    for page in Application.Document.Pages: 
        for visualization in page.Visuals: 
            if visualization.TypeId == VisualTypeIdentifiers.BarChart: 
                current_chart = visualization.As[BarChart]()
                current_chart.XAxis.ZoomRange = AxisRange(None, None)
            elif visualization.TypeId == VisualTypeIdentifiers.LineChart: 
                current_chart = visualization.As[LineChart]()
                current_chart.XAxis.ZoomRange = AxisRange(None, None)


def reset_doc_properties(): 

    Document.Properties['KPICategory'] = 'Resource Utilization'
    Document.Properties['AggregationLevels'] = 'RAW'
    Document.Properties['AggregationFunction'] = 'AVG'
    Document.Properties['NodeLevelKPIs'] = 'Average CPU Usage (%)' 
    Document.Properties['PTPKPIs'] = 'PTP Average Forward Delay (ns)'
    Document.Properties['KPICategoryInterface'] = 'Physical Port'
    Document.Properties['AggregationLevelInterface'] = 'RAW'
    Document.Properties['AggregationFunctionInterface'] = 'AVG'    
    Document.Properties['PhysicalPortKPIs'] = 'Ethernet Ingress Link Utilization (%)'
    Document.Properties['VlanKPIs'] = 'VLAN Ingress Utilization (%)'
    Document.Properties['PdhKPIs'] = 'PDH Port Availability (%)'
    Document.Properties['OpticalKPIs'] = 'Maximum Temperature (°C)' 
    

def add_marking_holder(): 

    for reset_page_title in reset_pages_list:
        page = get_page(reset_page_title)
        for visualization in page.Visuals: 
            if visualization.TypeId == VisualTypeIdentifiers.BarChart: 
                visualization = visualization.As[Visualization]()
                visualization.Data.Filterings.Add(Document.Data.Markings["Marking_dummy"])
            if visualization.TypeId == VisualTypeIdentifiers.KpiChart:
                chart = visualization.As[KpiChart]()
                chart.KpiCollection.Clear()


def get_page(page_name):

   for page in Document.Pages: 
      if page.Title == page_name: 
         return page


reset_doc_properties()
reset_marking_and_filtering()
reset_sliders()
add_marking_holder()