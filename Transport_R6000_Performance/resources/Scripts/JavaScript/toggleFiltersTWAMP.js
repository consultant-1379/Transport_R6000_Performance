MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

var targetDomId = "aggregationTWAMP"
var onLoadVal = $('#'+targetDomId+' .ComboBoxTextDivContainer').text();

if(onLoadVal == "ROP Data (No Aggregation)") {
	$(".rawFilterNodesTWAMP").show()
	$(".dayFilterNodesTWAMP").hide()
	$(".rawFilterTWAMP").show()
	$(".dayFilterTWAMP").hide()
}
else if(onLoadVal == "DAY"){
	$(".rawFilterNodesTWAMP").hide()
	$(".dayFilterNodesTWAMP").show()
	$(".rawFilterTWAMP").hide()
	$(".dayFilterTWAMP").show()
}

var myFunction = function(newValue){
	if(newValue == "ROP Data (No Aggregation)") {
		$(".rawFilterNodesTWAMP").show()
		$(".dayFilterNodesTWAMP").hide()
		$(".rawFilterTWAMP").show()
		$(".dayFilterTWAMP").hide()
	}	
	else if(newValue == "DAY"){
		$(".rawFilterNodesTWAMP").hide()
		$(".dayFilterNodesTWAMP").show()
		$(".rawFilterTWAMP").hide()
		$(".dayFilterTWAMP").show()
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