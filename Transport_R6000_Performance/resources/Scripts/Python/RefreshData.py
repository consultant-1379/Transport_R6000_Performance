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
# Name    : RefreshData.py
# Date    : 18/01/2024
# Revision: 1.0
# Purpose : Based on filter selection, fetches/refreshes data for the corresponding DoD data table
#
# Usage   : Transport Report
#

from Spotfire.Dxp.Framework.ApplicationModel import NotificationService
from Spotfire.Dxp.Framework.ApplicationModel import ProgressService
from datetime import datetime
from System import DateTime
from Spotfire.Dxp.Application.Visuals import *
node_level_kpis = "Node Level KPIs"
interface_level_kpis = "Interface Level KPIs"
twamp_kpis = "Transport Connectivity KPIs"
agg_doc_property_name_mapping = {node_level_kpis : 'AggregationLevels', interface_level_kpis : 'AggregationLevelInterface', twamp_kpis : 'AggregationLevelTWAMP'}
category_to_dt_mapping = {node_level_kpis : {'Resource Utilization' : 'IL_DC_E_IPTRANSPORT_GLOBAL_', 'PTP Clock' : 'IL_DC_E_IPTRANSPORT_PTP_'} , 
                          interface_level_kpis : {'Physical Port' : 'IL_DC_E_IPTRANSPORT_PORT_', 'VLAN Based Port' : 'IL_DC_E_IPTRANSPORT_DOT1Q_', 'PDH Port' : 'IL_DC_E_IPTRANSPORT_TDM1001_PDM_' , 'Optical' : 'IL_DC_E_IPTRANSPORT_SFP_HISTORY_'},
                          twamp_kpis : {'twamp' : 'IL_DC_E_IPTRANSPORT_TWAMP_V_'}
                          }
kpi_category_doc_prop_mapping = {node_level_kpis : 'KPICategory', interface_level_kpis : 'KPICategoryInterface', twamp_kpis : 'twamp'}
ps = Application.GetService[ProgressService]()
notify = Application.GetService[NotificationService]() 


def refresh_data():
    """Refreshes/loads respective data table based on current page, selected aggregation level, selected KPI category. Triggers the script 'GenerateCharts'.
        Arguments: NA
        Returns: NA
    """
    
    page = Document.ActivePageReference
    aggregation = Document.Properties[agg_doc_property_name_mapping[page.Title]]
    ps.CurrentProgress.ExecuteSubtask('Starting query')
    Document.Data.Tables[category_to_dt_mapping[page.Title][Document.Properties[kpi_category_doc_prop_mapping[page.Title]]] + aggregation ].ReloadAllData()
    for visualization in page.Visuals:
        if visualization.TypeId == VisualTypeIdentifiers.BarChart:
            visualization = visualization.As[Visualization]()
            for filtering in visualization.Data.Filterings:
                if filtering.Name == "Marking_dummy":
                    visualization.Data.Filterings.Remove(Document.Data.Markings["Marking_dummy"])
                    visualization.Data.Filterings.Remove(Document.Data.Markings["Marking_dummy"])
                    visualization.Data.Filterings.Remove(Document.Data.Markings["Marking_dummy"])
                    visualization.Data.Filterings.Remove(Document.Data.Markings["Marking_dummy"])
                    visualization.Data.Filterings.Remove(Document.Data.Markings["Marking_dummy"])
    Document.Properties['TriggerGenerateCharts'] = DateTime.UtcNow


def main():
    """Entry point of the scripts, calls refresh_data function to fetch data in NetAn data tables.
        Arguments: NA
        Returns: NA
    """
    try:
        refresh_data()
    except Exception as e:
        msg = "Something Went Wrong"
        notify.AddWarningNotification("Exception","Error in fetching data",msg)
        print("Exception: ", e)


ps.ExecuteWithProgress('Fetching data', 'Please be patient, this can take several minutes...', main)