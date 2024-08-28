MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

var targetDomId = "aggregation"
var onLoadVal = $('#'+targetDomId+' .ComboBoxTextDivContainer').text();


if(onLoadVal == "ROP Data (No Aggregation)" ) {
	$(".dayFilter").hide()
	$(".rawFilter").show()
	$(".dayFilterNodes").hide()
	$(".rawFilterNodes").show()
}
else if(onLoadVal == "DAY"){
	$(".dayFilter").show()
	$(".rawFilter").hide()
	$(".dayFilterNodes").show()
	$(".rawFilterNodes").hide()
}	

var myFunction = function(newValue){
	if(newValue=="ROP Data (No Aggregation)"){
		$(".dayFilter").hide()
	    $(".rawFilter").show()
	    $(".dayFilterNodes").hide()
	    $(".rawFilterNodes").show()
	}
	else if(newValue=="DAY"){
        $(".dayFilter").show()
        $(".rawFilter").hide()
        $(".dayFilterNodes").show()
        $(".rawFilterNodes").hide()
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