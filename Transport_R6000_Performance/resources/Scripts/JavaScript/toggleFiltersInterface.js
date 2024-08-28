MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
 
var targetDomId = "aggregationInterface"
var onLoadVal = $('#'+targetDomId+' .ComboBoxTextDivContainer').text();
 
if(onLoadVal == "ROP Data (No Aggregation)") {
    $(".dayFilterNodesInterface").hide()
    $(".rawFilterNodesInterface").show()
    $(".dayFilterInterface").hide()
    $(".rawFilterInterface").show()
}
else if(onLoadVal == "DAY"){
    $(".dayFilterNodesInterface").show()
    $(".rawFilterNodesInterface").hide()
    $(".dayFilterInterface").show()
    $(".rawFilterInterface").hide()
}
 
var myFunction = function(newValue){
    if(newValue == "ROP Data (No Aggregation)") {
        $(".dayFilterNodesInterface").hide()
        $(".rawFilterNodesInterface").show()
        $(".dayFilterInterface").hide()
        $(".rawFilterInterface").show()
    }
    else if(newValue == "DAY"){
        $(".dayFilterNodesInterface").show()
        $(".rawFilterNodesInterface").hide()
        $(".dayFilterInterface").show()
        $(".rawFilterInterface").hide()
    }
}
 
 
var target = document.getElementById(targetDomId)
var oldVal = target.innerText.trim()
 
var callback = function(mutations) {
 newVal=$('#'+targetDomId+' .ComboBoxTextDivContainer').text()
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