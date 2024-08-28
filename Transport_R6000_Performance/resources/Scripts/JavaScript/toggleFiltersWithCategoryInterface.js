MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
 
var targetDomId = "aggregationInterface"
var onLoadVal = $('#'+targetDomId+' .ComboBoxTextDivContainer').text();
 
var kpiCategory = "kpicategoryInterface"
var onLoadCategoryVal = $('#'+kpiCategory+' .ComboBoxTextDivContainer').text();
 
if(onLoadVal == "ROP Data (No Aggregation)" && onLoadCategoryVal == "Physical Port") {
    $(".FilterKPIPhyPort").show()
    $(".FilterKPIVlan").hide()
    $(".FilterKPIPdh").hide()
    $(".FilterKPIOptical").hide()
    $(".dayFilterNodesInterface").hide()
    $(".rawFilterNodesInterface").show()
    $(".dayFilterInterface").hide()
    $(".rawFilterInterface").show()
}
else if(onLoadVal == "ROP Data (No Aggregation)" && onLoadCategoryVal == "VLAN Based Port"){
    $(".FilterKPIPhyPort").hide()
    $(".FilterKPIVlan").show()
    $(".FilterKPIPdh").hide()
    $(".FilterKPIOptical").hide()
    $(".dayFilterNodesInterface").hide()
    $(".rawFilterNodesInterface").show()
    $(".dayFilterInterface").hide()
    $(".rawFilterInterface").show()
}
else if(onLoadVal == "ROP Data (No Aggregation)" && onLoadCategoryVal == "PDH Port"){
    $(".FilterKPIPhyPort").hide()
    $(".FilterKPIVlan").hide()
    $(".FilterKPIPdh").show()
    $(".FilterKPIOptical").hide()
    $(".dayFilterNodesInterface").hide()
    $(".rawFilterNodesInterface").show()
    $(".dayFilterInterface").hide()
    $(".rawFilterInterface").show()
}
else if(onLoadVal == "ROP Data (No Aggregation)" && onLoadCategoryVal == "Optical"){
    $(".FilterKPIPhyPort").hide()
    $(".FilterKPIVlan").hide()
    $(".FilterKPIPdh").hide()
    $(".FilterKPIOptical").show()
    $(".dayFilterNodesInterface").hide()
    $(".rawFilterNodesInterface").show()
    $(".dayFilterInterface").hide()
    $(".rawFilterInterface").show()
}
else if(onLoadVal == "DAY" && onLoadCategoryVal == "Physical Port"){
    $(".FilterKPIPhyPort").show()
    $(".FilterKPIVlan").hide()
    $(".FilterKPIPdh").hide()
    $(".FilterKPIOptical").hide()
    $(".dayFilterNodesInterface").show()
    $(".rawFilterNodesInterface").hide()
    $(".dayFilterInterface").show()
    $(".rawFilterInterface").hide()
}
else if(onLoadVal == "DAY" && onLoadCategoryVal == "VLAN Based Port"){
    $(".FilterKPIPhyPort").hide()
    $(".FilterKPIVlan").show()
    $(".FilterKPIPdh").hide()
    $(".FilterKPIOptical").hide()
    $(".dayFilterNodesInterface").show()
    $(".rawFilterNodesInterface").hide()
    $(".dayFilterInterface").show()
    $(".rawFilterInterface").hide()
}
else if(onLoadVal == "DAY" && onLoadCategoryVal == "PDH Port"){
    $(".FilterKPIPhyPort").hide()
    $(".FilterKPIVlan").hide()
    $(".FilterKPIPdh").show()
    $(".FilterKPIOptical").hide()
    $(".dayFilterNodesInterface").show()
    $(".rawFilterNodesInterface").hide()
    $(".dayFilterInterface").show()
    $(".rawFilterInterface").hide()
}
else if(onLoadVal == "DAY" && onLoadCategoryVal == "Optical"){
    $(".FilterKPIPhyPort").hide()
    $(".FilterKPIVlan").hide()
    $(".FilterKPIPdh").hide()
    $(".FilterKPIOptical").show()
    $(".dayFilterNodesInterface").show()
    $(".rawFilterNodesInterface").hide()
    $(".dayFilterInterface").show()
    $(".rawFilterInterface").hide()
}
 
var myFunction = function(newValue){
    var targetDomId = "aggregationInterface"
    var onLoadVal = $('#'+targetDomId+' .ComboBoxTextDivContainer').text();
    if(onLoadVal == "ROP Data (No Aggregation)" && newValue == "Physical Port") {
        $(".FilterKPIPhyPort").show()
        $(".FilterKPIVlan").hide()
        $(".FilterKPIPdh").hide()
        $(".FilterKPIOptical").hide()
        $(".dayFilterNodesInterface").hide()
        $(".rawFilterNodesInterface").show()
        $(".dayFilterInterface").hide()
        $(".rawFilterInterface").show()
    }
    else if(onLoadVal == "ROP Data (No Aggregation)" && newValue == "VLAN Based Port"){
        $(".FilterKPIPhyPort").hide()
        $(".FilterKPIVlan").show()
        $(".FilterKPIPdh").hide()
        $(".FilterKPIOptical").hide()
        $(".dayFilterNodesInterface").hide()
        $(".rawFilterNodesInterface").show()
        $(".dayFilterInterface").hide()
        $(".rawFilterInterface").show()
    }
    else if(onLoadVal == "ROP Data (No Aggregation)" && newValue == "PDH Port"){
        $(".FilterKPIPhyPort").hide()
        $(".FilterKPIVlan").hide()
        $(".FilterKPIPdh").show()
        $(".FilterKPIOptical").hide()
        $(".dayFilterNodesInterface").hide()
        $(".rawFilterNodesInterface").show()
        $(".dayFilterInterface").hide()
        $(".rawFilterInterface").show()
    }
    else if(onLoadVal == "ROP Data (No Aggregation)" && newValue == "Optical"){
        $(".FilterKPIPhyPort").hide()
        $(".FilterKPIVlan").hide()
        $(".FilterKPIPdh").hide()
        $(".FilterKPIOptical").show()
        $(".dayFilterNodesInterface").hide()
        $(".rawFilterNodesInterface").show()
        $(".dayFilterInterface").hide()
        $(".rawFilterInterface").show()
    }
    else if(onLoadVal == "DAY" && newValue == "Physical Port"){
        $(".FilterKPIPhyPort").show()
        $(".FilterKPIVlan").hide()
        $(".FilterKPIPdh").hide()
        $(".FilterKPIOptical").hide()
        $(".dayFilterNodesInterface").show()
        $(".rawFilterNodesInterface").hide()
        $(".dayFilterInterface").show()
        $(".rawFilterInterface").hide()
    }
    else if(onLoadVal == "DAY" && newValue == "VLAN Based Port"){
        $(".FilterKPIPhyPort").hide()
        $(".FilterKPIVlan").show()
        $(".FilterKPIPdh").hide()
        $(".FilterKPIOptical").hide()
        $(".dayFilterNodesInterface").show()
        $(".rawFilterNodesInterface").hide()
        $(".dayFilterInterface").show()
        $(".rawFilterInterface").hide()
    }
    else if(onLoadVal == "DAY" && newValue == "PDH Port"){
        $(".FilterKPIPhyPort").hide()
        $(".FilterKPIVlan").hide()
        $(".FilterKPIPdh").show()
        $(".FilterKPIOptical").hide()
        $(".dayFilterNodesInterface").show()
        $(".rawFilterNodesInterface").hide()
        $(".dayFilterInterface").show()
        $(".rawFilterInterface").hide()
    }
    else if(onLoadVal == "DAY" && newValue == "Optical"){
        $(".FilterKPIPhyPort").hide()
        $(".FilterKPIVlan").hide()
        $(".FilterKPIPdh").hide()
        $(".FilterKPIOptical").show()
        $(".dayFilterNodesInterface").show()
        $(".rawFilterNodesInterface").hide()
        $(".dayFilterInterface").show()
        $(".rawFilterInterface").hide()
    }
}
 
 
var target = document.getElementById(kpiCategory)
var oldVal = target.innerText.trim()
 
var callback = function(mutations) {
 newVal=$('#'+kpiCategory+' .ComboBoxTextDivContainer').text()
 if(newVal!=oldVal) myFunction(newVal)
 oldVal = newVal;
}
 
var observer = new MutationObserver(callback);
 
var opts = {
    childList: true,
    attributes: true,
    characterData: true,
    subtree: true
}
 
observer.observe(target,opts);