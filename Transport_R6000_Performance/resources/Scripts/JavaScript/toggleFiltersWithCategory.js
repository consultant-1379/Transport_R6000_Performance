MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
 
var targetDomId = "aggregation"
var onLoadVal = $('#'+targetDomId+' .ComboBoxTextDivContainer').text();
 
var kpiCategory = "kpicategory"
var onLoadCategoryVal = $('#'+kpiCategory+' .ComboBoxTextDivContainer').text();
 
if(onLoadVal == "ROP Data (No Aggregation)" && onLoadCategoryVal == "Resource Utilization") {
    $(".dayFilter").hide()
    $(".rawFilter").show()
    $(".dayFilterNodes").hide()
    $(".rawFilterNodes").show()
    $(".FilterKPI").show()
    $(".FilterKPIptp").hide()
}
else if(onLoadVal == "ROP Data (No Aggregation)" && onLoadCategoryVal == "PTP Clock"){
    $(".dayFilter").hide()
    $(".rawFilter").show()
    $(".dayFilterNodes").hide()
    $(".rawFilterNodes").show()
    $(".FilterKPI").hide()
    $(".FilterKPIptp").show()
}
else if(onLoadVal == "DAY" && onLoadCategoryVal == "Resource Utilization"){
    $(".dayFilter").show()
    $(".rawFilter").hide()
    $(".dayFilterNodes").show()
    $(".rawFilterNodes").hide()
    $(".FilterKPI").show()
    $(".FilterKPIptp").hide()
}
else if(onLoadVal == "DAY" && onLoadCategoryVal == "PTP Clock"){
    $(".dayFilter").show()
    $(".rawFilter").hide()
    $(".dayFilterNodes").show()
    $(".rawFilterNodes").hide()
    $(".FilterKPI").hide()
    $(".FilterKPIptp").show()
}  
 
var myFunction = function(newVal){
    var targetDomId = "aggregation"
    var onLoadVal = $('#'+targetDomId+' .ComboBoxTextDivContainer').text();
    if(onLoadVal=="ROP Data (No Aggregation)" && newVal == "Resource Utilization"){
        $(".dayFilter").hide()
        $(".rawFilter").show()
        $(".dayFilterNodes").hide()
        $(".rawFilterNodes").show()
        $(".FilterKPI").show()
        $(".FilterKPIptp").hide()
    }
    else if(onLoadVal=="ROP Data (No Aggregation)" && newVal == "PTP Clock"){
        $(".dayFilter").hide()
        $(".rawFilter").show()
        $(".dayFilterNodes").hide()
        $(".rawFilterNodes").show()
        $(".FilterKPI").hide()
        $(".FilterKPIptp").show()
    }  
    else if(onLoadVal=="DAY" && newVal == "Resource Utilization"){
        $(".dayFilter").show()
        $(".rawFilter").hide()
        $(".dayFilterNodes").show()
        $(".rawFilterNodes").hide()
        $(".FilterKPI").show()
        $(".FilterKPIptp").hide()
    }  
    else if(onLoadVal=="DAY" && newVal == "PTP Clock"){
        $(".dayFilter").show()
        $(".rawFilter").hide()
        $(".dayFilterNodes").show()
        $(".rawFilterNodes").hide()
        $(".FilterKPI").hide()
        $(".FilterKPIptp").show()
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