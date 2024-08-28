MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
var targetDomId = "LinkNameDataAvailabilityFlag"
var target = document.getElementById(targetDomId)

Date.prototype.today = function () { 
    return ((this.getDate() < 10)?"0":"") + this.getDate() +"/"+(((this.getMonth()+1) < 10)?"0":"") + (this.getMonth()+1) +"/"+ this.getFullYear();
}
Date.prototype.timeNow = function () {
     return ((this.getHours() < 10)?"0":"") + this.getHours() +":"+ ((this.getMinutes() < 10)?"0":"") + this.getMinutes() +":"+ ((this.getSeconds() < 10)?"0":"") + this.getSeconds();
}

var callback = function(mutations) {
	value=$('#LinkNameDataAvailabilityFlag input').val()
    if (value == "True"){
	createNoLinkLevelDataDialog()
    }
}

function createNoLinkLevelDataDialog(){
$("#spotfire-popup1").show();
var css = `

.spotfire-popup-overlay {
  position:fixed;
  top: -45px;
  left:0%; 
  width:1928px; 
  z-index:21;    
  bottom: 0px;
  right: 90%;
  background: rgba(0, 0, 0, 0.3);
}

.noLinkLevelDataDialog {
  margin: 0px auto;
  padding: 2px;
  background: #fff;
  color: #000;
  border-radius: 1px;
  width: 20%;
  min-height: 47px;
  height: auto;
  top: 41%;
  left: 38%;
  position: absolute;
}

/*header*/
.noLinkLevelDataDialog .header{
  border: 1px solid #c3c3c3;
  background: #f8f8f8;
  color: #000;
  font-weight: bold;
  padding: 8px;
  position: relative;
  margin-bottom: 10px;
}

/*title*/
.noLinkLevelDataDialog .title{
  display: inline;
  font-size: 13px;
  font-weight: bold;
  font-family: sans-serif;
}

/*Close*/
.noLinkLevelDataDialog .close {
  position: absolute;
  top: 2px;
  right: 9px;
  font-size: 24px;
  font-weight: bold;
  text-decoration: none;
  color: #000000;
}

.noLinkLevelDataDialog .close:hover {
  color: #000000;
}

/*layout*/
.noLinkLevelDataDialog .layout{
  padding-top: 15px;
  padding-left: 6px;
  padding-bottom: 9px;
  font-size: 12px;
  font-family: sans-serif;
  max-height: 160px;
  overflow: auto;
}

/*layout-bottom*/
.noLinkLevelDataDialog .layout-bottom{
  padding-top: 10px;
  padding-left: 6px;
  padding-bottom: 9px;
  font-size: 12px;
}
	
/*layout-top*/
.noLinkLevelDataDialog .layout-top{
  padding-top: 10px;
  padding-left: 6px;
  padding-bottom: 9px;
  font-size: 12px;
}
	
/*Footer*/
.noLinkLevelDataDialog .footer{
  display: flex;
  justify-content: flex-end;
  //gap: 2px ;
  margin-top: 30px;
  border-top: 1px solid #c3c3c3;
  padding-top : 10px;
  margin-bottom : 10px;
  padding-inline-end: 7px;
}

/*ok_button*/
.noLinkLevelDataDialog .proceed {
  //position: absolute;
  text-align: center;
  cursor: pointer;
  bottom: 20px;
  right: 30px;
  background: #0074D9;
  color: #fff;
  width: 62px;
  border-radius: 1px;
  font-size: 13px;
  height: 27px;
  padding-top: 9px;
  font-weight: normal;
}

.noLinkLevelDataDialog .proceed:hover {
  color: #fff;
  background: #0074D9;
}

/*cancel_button*/
.noLinkLevelDataDialog .cancel {
  //position: absolute;
  text-align: center;
  cursor: pointer;
  bottom: 20px;
  right: 1px;
  background: grey;
  color: #fff;
  width: 62px;
  border-radius: 1px;
  font-size: 13px;
  height: 27px;
  padding-top: 9px;
  font-weight: normal;
  margin-right: 5px;
}

.noLinkLevelDataDialog .cancel:hover {
  color: #fff;
  background: grey;
}

.noLinkLevelDataDialog .dialog-confirm {
  max-height: 30%;
  overflow: auto;
}
`;

// Inject the CSS into an HTML tag which has the id StyleDiv
$("<style/>").text(css).appendTo($("#styleDiv"));

// override the click events and apply styles for popups to open and close
$("#deleteReportButton").click(function(event){
	event.preventDefault();
	$('.spotfire-popup-overlay').css("visibility", "visible");
	$('.spotfire-popup-overlay').css("opacity", 1);
});

$(".close").click(function(event){
	event.preventDefault();
	$('.spotfire-popup-overlay').css("visibility", "hidden");
	$('.spotfire-popup-overlay').css("opacity", 0);
	$('#ReturnToNodePageFromLinkLevelTrigger input').val(new Date().today() + " @ " + new Date().timeNow())
	$("#ReturnToNodePageFromLinkLevelTrigger input").focus();
	$("#ReturnToNodePageFromLinkLevelTrigger input").blur();
});

$(".proceed").click(function(event){
	event.preventDefault();
	$("#deleteBtnInput input").val('Other').blur();
	$('.spotfire-popup-overlay').css("visibility", "hidden");
	$('.spotfire-popup-overlay').css("opacity", 0);
	$('#IdOkayBtuLabel input').val(new Date().today() + " @ " + new Date().timeNow())
	$("#IdOkayBtuLabel input").focus();
	$("#IdOkayBtuLabel input").blur();
});

$(".cancel").click(function(event){
	event.preventDefault();
	$('.spotfire-popup-overlay').css("visibility", "hidden");
	$('.spotfire-popup-overlay').css("opacity", 0);
	$('#ReturnToNodePageFromLinkLevelTrigger input').val(new Date().today() + " @ " + new Date().timeNow())
	$("#ReturnToNodePageFromLinkLevelTrigger input").focus();
	$("#ReturnToNodePageFromLinkLevelTrigger input").blur();
});

}

var observer = new MutationObserver(callback);
var opts = {
    childList: true, 
    attributes: true, 
    characterData: true, 
    subtree: true
}
observer.observe(target,opts);
