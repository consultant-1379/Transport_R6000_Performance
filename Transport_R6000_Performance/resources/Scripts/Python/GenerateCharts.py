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
# Name    : GenerateCharts.py
# Date    : 18/01/2024
# Revision: 1.0
# Purpose : Generates line and bar charts based on selected filters
#
# Usage   : Transport Report
#

from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Application.Visuals import *
from System import DateTime

node_level_kpis = "Node Level KPIs"
interface_level_kpis = "Interface Level KPIs"
twamp_kpis = "Transport Connectivity KPIs"
agg_doc_property_name_mapping = {node_level_kpis : 'AggregationLevels', interface_level_kpis : 'AggregationLevelInterface', twamp_kpis : 'AggregationLevelTWAMP'}
agg_function_doc_property_name_mapping = {node_level_kpis : 'AggregationFunction', interface_level_kpis: 'AggregationFunctionInterface', twamp_kpis : 'aggregationFunctionTWAMP'}
category_to_dt_mapping = {node_level_kpis : {'Resource Utilization' : 'IL_DC_E_IPTRANSPORT_GLOBAL_', 'PTP Clock' : 'IL_DC_E_IPTRANSPORT_PTP_'} , 
                          interface_level_kpis : {'Physical Port' : 'IL_DC_E_IPTRANSPORT_PORT_', 'VLAN Based Port' : 'IL_DC_E_IPTRANSPORT_DOT1Q_', 'PDH Port' : 'IL_DC_E_IPTRANSPORT_TDM1001_PDM_' , 'Optical' : 'IL_DC_E_IPTRANSPORT_SFP_HISTORY_'},
                          twamp_kpis : {'twamp' : 'IL_DC_E_IPTRANSPORT_TWAMP_V_'}
                          }
kpi_list_mapping = {'Resource Utilization': 'NodeLevelKPIs', 'PTP Clock': 'PTPKPIs', 'Physical Port' : 'PhysicalPortKPIs', 'VLAN Based Port' : 'VlanKPIs', 'PDH Port' : 'PdhKPIs' , 'Optical' : 'OpticalKPIs', 'twamp' : 'TWAMPKPIs'}
kpi_category_doc_prop_mapping = {node_level_kpis : 'KPICategory', interface_level_kpis : 'KPICategoryInterface', twamp_kpis : 'twamp'}
date_time_column_mapping = {'RAW': 'DATETIME_ID', 'DAY': 'DATE_ID'}
chart_flags = ['bar', 'line']
filtered_page_name_mapping = {node_level_kpis : 'Node Level KPIs - Filtered Data', interface_level_kpis : 'Interface Level KPIs - Filtered Data', twamp_kpis : 'Transport Connectivity KPIs - Filtered Data'}
kpi_marking_mapping = {node_level_kpis : 'NodeLevelKPI', interface_level_kpis : 'InterfaceLevelKPIs', twamp_kpis : 'twampKPIs' }

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
        kpi_category_prop = kpi_category_doc_prop_mapping[page.Title]
        table = category_to_dt_mapping[page.Title][Document.Properties[kpi_category_prop]]        
        properties_dict = {'dt':Document.Data.Tables[table + agg_flag],'x_axis_expression':date_time_column_mapping[agg_flag],'y_axis_expression':'$map("{0}($esc(${{{1}}}))", ",")'.format(aggregation_function, kpi_list_mapping[Document.Properties[kpi_category_doc_prop_mapping[page.Title]]])}
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

def get_filtered_data_page_table(page, aggregation):
    """Gets filtered data page and table details 
        Arguments: 
            page {object} --> Active page object
            aggregation {string} --> Selected aggregation ('RAW' or 'DAY')
        Returns: NA
    """
    kpi_category_prop = kpi_category_doc_prop_mapping[page.Title]
    table = Document.Data.Tables[category_to_dt_mapping[page.Title][Document.Properties[kpi_category_prop]] + aggregation]
    filtered_data_page = filtered_page_name_mapping[page.Title]
    set_filtered_data_page_table(filtered_data_page, table, page )

def set_filtered_data_page_table(page_name, data_table, page):
    """Sets chart properties.
        Arguments: 
            page_name {string} --> Name of the filtered data page
            data_table {object} --> Filtered data table
            page {object} --> Active page object
        Returns: NA
    """
    for orig_page in Document.Pages: 
      if orig_page.Title == page_name: 
          for vis in orig_page.Visuals:
            if vis.Title == 'FilteredDataVis':
                vis = vis.As[Visualization]()
                vis.TableColumns.Clear()
                vis.Data.DataTableReference = data_table
                vis.Data.LimitingMarkingsEmptyBehavior = LimitingMarkingsEmptyBehavior.ShowAll
                vis.Data.Filterings.Add(Document.Data.Markings[kpi_marking_mapping[page.Title]])
                for column in data_table.Columns:
                    vis.TableColumns.Add(column)

def main():
    """Gets active page, aggregation details and calls generate_charts function to generate line and bar charts. Triggers 'SetKPIChart' script.
        Arguments: NA
        Returns: NA
    """
    initial_page = Document.ActivePageReference
    aggregation = Document.Properties[agg_doc_property_name_mapping[initial_page.Title]]
    aggregation_function = Document.Properties[agg_function_doc_property_name_mapping[initial_page.Title]]
    if initial_page.Title != 'Home':
        generate_charts(initial_page,aggregation,aggregation_function)
        get_filtered_data_page_table(initial_page, aggregation)
        Document.Properties['TriggerSetKPIChart'] = DateTime.UtcNow

main()
