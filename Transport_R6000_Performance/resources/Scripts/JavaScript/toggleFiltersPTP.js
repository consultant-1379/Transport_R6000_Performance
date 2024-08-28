MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

var targetDomId = "aggregationPTP"
var onLoadVal=$('#'+targetDomId+' .ComboBoxTextDivContainer').text();
 
if(onLoadVal=="ROP Data (No Aggregation)"){
	console.log("word")
	console.log(onLoadVal)
	$(".dayFilterPTP").hide()
	$(".rawFilterPTP").show()
	$(".dayFilterNodesPTP").hide()
	$(".rawFilterNodesPTP").show()
	$(".dayFilterKPIPTP").hide()
	$(".rawFilterKPIPTP").show()}
	else if(onLoadVal=="DAY"){
		$(".dayFilterPTP").show()
	    $(".rawFilterPTP").hide()
		$(".dayFilterNodesPTP").show()
	    $(".rawFilterNodesPTP").hide()
		$(".rawFilterKPIPTP").hide()
		$(".dayFilterKPIPTP").show()
		}	

var myFunction = function(oldValue,newValue){
  if(newValue=="ROP Data (No Aggregation)"){
	console.log("word")
	console.log(newValue)
	value=$('#dataflag input').val()
	$(".dayFilterPTP").hide()
	$(".rawFilterPTP").show()
	$(".dayFilterNodesPTP").hide()
	$(".rawFilterNodesPTP").show()
	$(".dayFilterKPIPTP").hide()
	$(".rawFilterKPIPTP").show()}
	else if(newValue=="DAY"){
		$(".dayFilterPTP").show()
	    $(".rawFilterPTP").hide()
		$(".dayFilterNodesPTP").show()
	    $(".rawFilterNodesPTP").hide()
		$(".rawFilterKPIPTP").hide()
		$(".dayFilterKPIPTP").show()
	    }	
}

var target = document.getElementById(targetDomId)
var oldVal = target.innerText.trim()

var callback = function(mutations) {
 newVal=$('#'+targetDomId+' .ComboBoxTextDivContainer').text()
 if(newVal!=oldVal) myFunction(oldVal,newVal)
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