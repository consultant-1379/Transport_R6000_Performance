# ********************************************************************
# Ericsson Inc.                                                 SCRIPT
# ********************************************************************
#
#
# (c) Ericsson Inc. 2024 - All rights reserved.
#
# The copyright to the computer program(s) herein is the property
# of Ericsson Inc. The programs may be used and/or copied only with
# the written permission from Ericsson Inc. or in accordance with the
# terms and conditions stipulated in the agreement/contract under
# which the program(s) have been supplied.
#
# ********************************************************************
# Name    : GenerateInterfaceDetails.py
# Date    : 18/01/2024
# Revision: 1.0
# Purpose : Generates line and bar charts based on selected filters
#
# Usage   : Transport Report
#

from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Application.Visuals import *
from System import DateTime

interface_level_kpis = "Interface Level KPIs"
agg_doc_property_name_mapping = {interface_level_kpis : 'AggregationLevelInterface'}
agg_function_doc_property_name_mapping = {interface_level_kpis: 'AggregationFunctionInterface'}
category_to_dt_mapping = { interface_level_kpis : {'Physical Port' : 'IL_DC_E_IPTRANSPORT_PORT_', 'VLAN Based Port' : 'IL_DC_E_IPTRANSPORT_DOT1Q_', 'PDH Port' : 'IL_DC_E_IPTRANSPORT_TDM1001_PDM_' , 'Optical' : 'IL_DC_E_IPTRANSPORT_SFP_HISTORY_'}}
kpi_list_mapping = {'PTP Clock': 'PTPKPIs', 'Physical Port' : 'PhysicalPortKPIs', 'VLAN Based Port' : 'VlanKPIs', 'PDH Port' : 'PdhKPIs' , 'Optical' : 'OpticalKPIs', 'twamp' : 'TWAMPKPIs'}
kpi_category_doc_prop_mapping = {interface_level_kpis : 'KPICategoryInterface'}
date_time_column_mapping = {'RAW': 'DATETIME_ID', 'DAY': 'DATE_ID'}
chart_flags = ['bar', 'line']

def get_bar_or_line_chart(page, chart_flag):
    """Gets line and chart visualization objects.
        Arguments: 
            page {object} --> Active page object
            chart_flag {string} --> 'bar' or 'line'
        Returns: 
            vis {object} --> Visualization object
    """
    if chart_flag == 'bar':
        for vis in page.Visuals:
            if vis.TypeId == VisualTypeIdentifiers.BarChart:
               return vis.As[BarChart]()
    else:
        for vis in page.Visuals:
            if vis.TypeId == VisualTypeIdentifiers.LineChart:
                return vis.As[LineChart]()

def generate_charts(page, agg_flag, aggregation_function):
    """Gets chart properties based on filter selection and calls function 'set_bar_line_chart_properties' to set those properties.
        Arguments: 
            page {object} --> Active page object
            agg_flag {string} --> Selected aggregation ('RAW' or 'DAY')
            aggregation_function {string} --> Selected aggregation function ('AVG', 'MAX' or 'MIN')
        Returns: NA
    """
    for chart_flag in chart_flags:
        charts_list = []
        properties_dict = {}
        chart = get_bar_or_line_chart(page, chart_flag)
        charts_list.append(chart)
        kpi_category_prop = kpi_category_doc_prop_mapping[interface_level_kpis]
        table = category_to_dt_mapping[interface_level_kpis][Document.Properties[kpi_category_prop]]        
        properties_dict = {'dt':Document.Data.Tables[table + agg_flag],'x_axis_expression':date_time_column_mapping[agg_flag],'y_axis_expression':'$map("{0}($esc(${{{1}}}))", ",")'.format(aggregation_function, kpi_list_mapping[Document.Properties[kpi_category_doc_prop_mapping[interface_level_kpis]]])}
        set_bar_line_chart_properties(charts_list, properties_dict, chart_flag)

def set_bar_line_chart_properties(charts_list, properties_dict, chart_flag):
    """Sets chart properties.
        Arguments: 
            charts_list {list[object]} --> List of chart objects
            properties_dict {dictionary} --> Dictionary containing chart properties
            chart_flag {string} --> 'bar' or 'line'
        Returns: NA
    """
    for chart in charts_list:
        chart.Data.DataTableReference = properties_dict['dt']
        chart.YAxis.Expression = properties_dict['y_axis_expression']
        if chart_flag == 'line':
            chart.XAxis.Expression = properties_dict['x_axis_expression']  

def main():
    """Gets active page, aggregation details and calls generate_charts function to generate line and bar charts. Triggers 'SetKPIChart' script.
        Arguments: NA
        Returns: NA
    """
    aggregation = Document.Properties[agg_doc_property_name_mapping[interface_level_kpis]]
    aggregation_function = Document.Properties[agg_function_doc_property_name_mapping[interface_level_kpis]]
    generate_charts(Document.Pages[3],aggregation,aggregation_function)
    
main()
