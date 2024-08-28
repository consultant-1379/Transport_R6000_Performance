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
# Name    : SetKpiVis.py
# Date    : 18/01/2024
# Revision: 1.0
# Purpose : Configures KPI chart and its' tiles based on KPI and aggregation function filter selection
#
# Usage   : Transport Report
#

from Spotfire.Dxp.Application.Visuals import *
from System.Drawing import Color
from Spotfire.Dxp.Application.Visuals.ConditionalColoring import RuleComparisonOperator, ConditionValue
from Spotfire.Dxp.Data import * 
from Spotfire.Dxp.Data.Formatters import *
from System import DateTime

node_level_kpis = "Node Level KPIs"
interface_level_kpis = "Interface Level KPIs"
twamp_kpis = "Transport Connectivity KPIs"
agg_doc_property_name_mapping = {node_level_kpis : 'AggregationLevels', interface_level_kpis : 'AggregationLevelInterface', twamp_kpis : 'AggregationLevelTWAMP'}
kpi_list_mapping = {'Resource Utilization': 'NodeLevelKPIs', 'PTP Clock': 'PTPKPIs', 'Physical Port' : 'PhysicalPortKPIs', 'VLAN Based Port' : 'VlanKPIs', 'PDH Port' : 'PdhKPIs' , 'Optical' : 'OpticalKPIs', 'twamp' : 'TWAMPKPIs'}
category_to_dt_mapping = {node_level_kpis : {'Resource Utilization' : 'IL_DC_E_IPTRANSPORT_GLOBAL_', 'PTP Clock' : 'IL_DC_E_IPTRANSPORT_PTP_'} , 
                          interface_level_kpis : {'Physical Port' : 'IL_DC_E_IPTRANSPORT_PORT_', 'VLAN Based Port' : 'IL_DC_E_IPTRANSPORT_DOT1Q_', 'PDH Port' : 'IL_DC_E_IPTRANSPORT_TDM1001_PDM_' , 'Optical' : 'IL_DC_E_IPTRANSPORT_SFP_HISTORY_'},
                          twamp_kpis : {'twamp' : 'IL_DC_E_IPTRANSPORT_TWAMP_V_'}
                          }
agg_function_doc_property_name_mapping = {node_level_kpis : 'AggregationFunction', interface_level_kpis: 'AggregationFunctionInterface', twamp_kpis : 'aggregationFunctionTWAMP'}
kpi_category_doc_prop_mapping = {node_level_kpis : 'KPICategory', interface_level_kpis : 'KPICategoryInterface', twamp_kpis : 'twamp'}
kpi_marking_mapping = {node_level_kpis : 'NodeLevelKPI', interface_level_kpis : 'InterfaceLevelKPIs', twamp_kpis : 'twampKPIs' }

def add_kpi_chart_tile(chart, page, kpi, aggregation):
    """Adds KPI chart title for each selected KPI.
        Arguments: 
            chart {object} --> Visualization object
            page {object} --> Active page object
            kpi {string} --> selected KPI
            aggregation {string} --> 'RAW' or 'DAY'
        Returns: NA
    """
    kpi_content = chart.KpiCollection.AddNew()
    kpi_chart_tile = kpi_content.Visualization
    kpi_chart_tile.Data.LimitingMarkingsEmptyBehavior = LimitingMarkingsEmptyBehavior.ShowAll
    kpi_chart_tile.Data.DataTableReference = Document.Data.Tables[category_to_dt_mapping[page.Title][Document.Properties[kpi_category_doc_prop_mapping[page.Title]]] + aggregation]
    kpi_chart_tile.Data.Filterings.Add(Document.Data.Markings[kpi_marking_mapping[page.Title]])
    kpi_chart_tile.YAxis.Expression = '{agg}([{kpi}]) as [Total {kpi_name_processed} per Node]'.format(kpi=kpi, kpi_name_processed=kpi, agg = "SUM")
    set_coloring(page, kpi, kpi_chart_tile)
    set_x_tile_axes_expressions(kpi_chart_tile)       

def set_coloring(page, kpi, kpi_chart_tile):
    """Sets color properties for each KPI tile.
        Arguments: 
            page {object} --> Active page object
            kpi {string} --> selected KPI
            kpi_chart_tile {object} --> Visualization object
        Returns: NA
    """
    kpi_chart_tile.ColorAxis.Expression = Document.Properties[agg_function_doc_property_name_mapping[page.Title]] + '([' +kpi+ '])'
    kpi_chart_tile.ShowSparkline = False
    kpi_visualization_coloring = kpi_chart_tile.ColorAxis.Coloring
    kpi_visualization_coloring.Clear()
    color_rule = kpi_visualization_coloring.AddThresholdColorRule(RuleComparisonOperator.GreaterOrEqual, ConditionValue.CreateLiteral(-1000000000), Color.FromArgb(160, 160, 160))
    color_rule.ManualDisplayName = "All values"

def set_x_tile_axes_expressions(kpi_chart_tile):
    """Sets X-axis value for the tiles.
        Arguments: 
            kpi {string} --> selected KPI
            kpi_chart_tile {object} --> Visualization object
        Returns: NA
    """
    kpi_chart_tile.XAxis.Expression = 'NE_NAME'
    kpi_chart_tile.TileAxis.Expression = '<[NE_NAME]>'

def configure_kpi_chart_vis(page, aggregation):
    """Gets selected KPI details and calls add_kpi_chart_tile to add KPI chart.
        Arguments: 
            page {object} --> Active page object
            aggregation {string} --> 'RAW' or 'DAY'
        Returns: NA
    """
    for vis in page.Visuals:
        if vis.TypeId == VisualTypeIdentifiers.KpiChart:
            chart = vis.As[KpiChart]()
            chart.KpiCollection.Clear()
            kpi_doc_prop = Document.Properties[kpi_list_mapping[Document.Properties[kpi_category_doc_prop_mapping[page.Title]]]]
            for kpi in kpi_doc_prop:
                add_kpi_chart_tile(chart, page, kpi, aggregation)               

def main():
    """Gets active page, aggregation details and calls configure_kpi_chart_vis function to generate KPI chart.
        Arguments: NA
        Returns: NA
    """
    initial_page = Document.ActivePageReference
    if initial_page.Title != 'Home':
        aggregation = Document.Properties[agg_doc_property_name_mapping[initial_page.Title]] 
        configure_kpi_chart_vis(initial_page,aggregation)
    if initial_page.Title == interface_level_kpis:
        Document.Properties['TriggerGenerateInterfaceDetails'] = DateTime.UtcNow

main()