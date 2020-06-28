/*
jQWidgets v9.0.0 (2020-Jan)
Copyright (c) 2011-2020 jQWidgets.
License: https://jqwidgets.com/license/
*/
/* eslint-disable */

(function(a){a.jqx.jqxWidget("jqxComplexInput","",{});a.extend(a.jqx._jqxComplexInput.prototype,{defineInstance:function(){var b={width:null,height:null,decimalNotation:"default",value:"",spinButtons:false,spinButtonsStep:1,placeHolder:"",roundedCorners:true,disabled:false,rtl:false,changeType:null,hint:true,template:"",events:["change"]};if(this===a.jqx._jqxComplexInput.prototype){return b}a.extend(true,this,b);return b},createInstance:function(){var b=this;b._firefox=a.jqx.browser.browser==="mozilla";b._currentNumber={};b._allowedCharacters=new RegExp(/([\+\-\.0-9i])/i);b.render()},render:function(){var e=this;if(e.isMaterialized()){var i=a("<label></label");if(this.hint){i[0].innerHTML=this.placeHolder}i.addClass(e.toThemeProperty("jqx-input-label"));var f=a("<span></span>");f.addClass(e.toThemeProperty("jqx-input-bar"));if(e.element.nodeName.toUpperCase()==="INPUT"){var l=a("<div></div>");l.addClass(e.toThemeProperty("jqx-input-group jqx-complex-input-group"));this.host.after(l);var j=this.element;var d=this.host.data();l.append(j);l.append(i);l.append(f)}else{this.host.append(i);this.host.append(f);this.host.addClass(e.toThemeProperty("jqx-input-group jqx-complex-input-group"));f.css("top",6+this.element.offsetHeight)}e.bar=f;e.label=i}if(e.element.nodeName.toUpperCase()==="DIV"){e.baseHost=e.host;var d=e.host.data();e.host=e.baseHost.children("input");e.element=e.host[0];e.host.data(d)}if(e.spinButtons===true){if(!e.baseHost){throw new Error("jqxComplexInput: Invalid HTML structure. Please initialize the complex input from a div with an input and another div inside.")}e._appendSpinButtons()}e._addClasses();e._setSize();e._removeHandlers();e._addHandlers();if(e.decimalNotation==="exponential"&&e.value.toLowerCase().indexOf("e")!==-1){var g=e._exponentialToDecimal(e.value);var h=g.realPart;var c=g.imaginaryPart;var b=c<0?"-":"+";var k=h+" "+b+" "+Math.abs(c)+"i";e._currentNumber={value:k,realPart:h,imaginaryPart:c}}else{e._currentNumber={value:e.value,realPart:e._getReal(e.value),imaginaryPart:e._getImaginary(e.value)}}if(e.decimalNotation==="default"){e.element.value=e.value}else{e._setNotation()}e._refreshPlaceHolder()},refresh:function(b){if(b!==true){this.render()}},destroy:function(){var b=this;b._removeHandlers();b.host.destroy()},val:function(e){var d=this;if(typeof e==="string"||typeof e==="object"&&a.isEmptyObject(e)===false){var h,c;if(typeof e==="string"){e=e.toLowerCase();if(e.indexOf("e")===-1){h=d._getReal(e);c=d._getImaginary(e)}else{var g=d._exponentialToDecimal(e);h=g.realPart*1;c=g.imaginaryPart*1}}else{if(typeof e==="object"&&a.isEmptyObject(e)===false){h=e.real;c=e.imaginary}}var b=c>=0?"+":"-";var f=h+" "+b+" "+Math.abs(c)+"i";if(f!==d._currentNumber.value){d.element.value=f;d._onChange(d.value);if(d.decimalNotation!=="default"){d._setNotation()}}}else{return d.element.value}},getReal:function(){return this._currentNumber.realPart},_getReal:function(f){if(!f||(typeof f==="object"&&a.isEmptyObject(f)===true)){f=this.element.value}var c=a.trim(f),e="";if((f.match(/i/g)||[]).length===0){return parseFloat(c)}if(f.charAt(0)==="+"){c=c.slice(1,f.length)}else{if(f.charAt(0)==="-"){c=c.slice(1,f.length);e="-"}}function g(h){c=c.slice(0,h);c=a.trim(c);return parseFloat(e+""+c)}var b=c.indexOf("+");if(b!==-1){return g(b)}var d=c.indexOf("-");if(d!==-1){return g(d)}return 0},getImaginary:function(){return this._currentNumber.imaginaryPart},_getImaginary:function(f){if(!f||(typeof f==="object"&&a.isEmptyObject(f)===true)){f=this.element.value}if((f.match(/i/g)||[]).length===0){return 0}var e=a.trim(f),d="";if(e.charAt(0)==="-"||e.charAt(0)==="+"){d=e.charAt(0)==="-"?"-":"+";e=a.trim(e.slice(1,f.length))}function g(i,h){e=e.slice(i+1,e.indexOf("i"));e=a.trim(e);if(e===""){e=1}return parseFloat(h+""+e)}var b=e.indexOf("+");if(b!==-1){return g(b,"+")}var c=e.indexOf("-");if(c!==-1){return g(c,"-")}e=d+""+e.slice(0,e.indexOf("i"));if(e===""||e==="+"){return 1}else{if(e==="-"){return -1}else{return parseFloat(e)}}},getDecimalNotation:function(f,c){var e=this;function d(k){var j=k.indexOf("e");var i=k.slice(j+1);var h=k.slice(0,j+1);h=h.replace("e","×10");h+=e._toSuperScript(i);h=h.replace("+","");return h}function b(n){var m=n.indexOf("e");var l=n.slice(m+1);var j=n.slice(0,m);var k=parseInt(l,10)%3;j=j*Math.pow(10,k);var i=n.slice(0,m).length-k-2;if(i>=0){j=j.toFixed(i)}var h=j+"×10"+e._toSuperScript((parseInt(l,10)-k).toString());return h}if(f==="real"){f=e._currentNumber.realPart}else{if(f==="imaginary"){f=e._currentNumber.imaginaryPart}}var g=f.toExponential();if(c==="scientific"){return d(g)}else{if(c==="engineering"){return b(g)}else{return g}}},propertyChangedHandler:function(e,j,d,h){var g=this;if(h!==d){switch(j){case"template":if(e.template){e._upbutton.removeClass(g.toThemeProperty("jqx-"+d));e._downbutton.removeClass(g.toThemeProperty("jqx-"+d));e._upbutton.addClass(g.toThemeProperty("jqx-"+e.template));e._downbutton.addClass(g.toThemeProperty("jqx-"+e.template))}break;case"width":case"height":e._setSize();break;case"decimalNotation":if(h==="default"){e.element.value=e._currentNumber.value}else{e._setNotation()}break;case"value":e.element.value=h;e._onChange(d);break;case"spinButtons":var l=function(){e.host.removeClass(e.toThemeProperty("jqx-rc-all"));if(e.rtl===false){e.host.addClass(e.toThemeProperty("jqx-rc-l"));e._spinButtonsContainer.addClass(e.toThemeProperty("jqx-rc-r"))}else{e.host.addClass(e.toThemeProperty("jqx-rc-r"));e._spinButtonsContainer.addClass(e.toThemeProperty("jqx-rc-l"))}};if(e._spinButtonsContainer){var k=e.host.width();var i=e._spinButtonsContainer.outerWidth();if(h===false){e.host.width(k+i);e._spinButtonsContainer.hide();e.host.addClass(e.toThemeProperty("jqx-rc-all"))}else{e.host.width(k-i);e._spinButtonsContainer.show();l()}}else{if(h===true){var m=a("<div></div>");if(e.baseHost){e.host.after(m);e.render()}else{var c=e.element.id;e.host.removeAttr("id");e.host.wrap('<div id="'+c+'" style="display: inline-block;"></div>');var b=a("#"+c);b.append(m);var f=e.host.data();f.jqxComplexInput.host=b;f.jqxComplexInput.element=b[0];e.baseHost=b;e.baseHost.data(f);e.render()}l()}}break;case"placeHolder":e._refreshPlaceHolder(d);break;case"roundedCorners":if(e._spinButtonsContainer){if(h===true){if(e.rtl===false){e.host.addClass(e.toThemeProperty("jqx-rc-l"));e._spinButtonsContainer.addClass(e.toThemeProperty("jqx-rc-r"))}else{e.host.addClass(e.toThemeProperty("jqx-rc-r"));e._spinButtonsContainer.addClass(e.toThemeProperty("jqx-rc-l"))}}else{if(e.rtl===false){e.host.removeClass(e.toThemeProperty("jqx-rc-l"));e._spinButtonsContainer.removeClass(e.toThemeProperty("jqx-rc-r"))}else{e.host.removeClass(e.toThemeProperty("jqx-rc-r"));e._spinButtonsContainer.removeClass(e.toThemeProperty("jqx-rc-l"))}}}else{if(h===true){e.host.addClass(e.toThemeProperty("jqx-rc-all"))}else{e.host.removeClass(e.toThemeProperty("jqx-rc-all"))}}break;case"disabled":if(h===true){e.host.attr("disabled",true);e.host.addClass(e.toThemeProperty("jqx-fill-state-disabled jqx-input-disabled"));if(e._spinButtonsContainer){e._spinButtonsContainer.addClass(e.toThemeProperty("jqx-fill-state-disabled"))}}else{e.host.removeAttr("disabled");e.host.removeClass(e.toThemeProperty("jqx-fill-state-disabled jqx-input-disabled"));if(e._spinButtonsContainer){e._spinButtonsContainer.removeClass(e.toThemeProperty("jqx-fill-state-disabled"))}}break;case"rtl":if(e._spinButtonsContainer){if(h===true){e.host.addClass(e.toThemeProperty("jqx-complex-input-child-rtl"));e._spinButtonsContainer.removeClass(e.toThemeProperty("jqx-complex-input-spin-buttons-container-ltr"));e._spinButtonsContainer.addClass(e.toThemeProperty("jqx-complex-input-child-rtl jqx-complex-input-spin-buttons-container-rtl"));if(e.roundedCorners===true){e.host.removeClass(e.toThemeProperty("jqx-rc-l"));e.host.addClass(e.toThemeProperty("jqx-rc-r"));e._spinButtonsContainer.removeClass(e.toThemeProperty("jqx-rc-r"));e._spinButtonsContainer.addClass(e.toThemeProperty("jqx-rc-l"))}}else{e.host.removeClass(e.toThemeProperty("jqx-complex-input-child-rtl"));e._spinButtonsContainer.removeClass(e.toThemeProperty("jqx-complex-input-child-rtl jqx-complex-input-spin-buttons-container-rtl"));e._spinButtonsContainer.addClass(e.toThemeProperty("jqx-complex-input-spin-buttons-container-ltr"));if(e.roundedCorners===true){e.host.removeClass(e.toThemeProperty("jqx-rc-r"));e.host.addClass(e.toThemeProperty("jqx-rc-l"));e._spinButtonsContainer.removeClass(e.toThemeProperty("jqx-rc-l"));e._spinButtonsContainer.addClass(e.toThemeProperty("jqx-rc-r"))}}}break;case"theme":a.jqx.utilities.setTheme(d,h,e.host);break}}},_raiseEvent:function(f,c){if(c===undefined){c={owner:null}}var d=this.events[f];c.owner=this;var e=new a.Event(d);e.owner=this;c.type=this.changeType;this.changeType=null;e.args=c;if(e.preventDefault){e.preventDefault()}var b=this.host.trigger(e);return b},_appendSpinButtons:function(){var b=this;b._spinButtonsContainer=a(b.baseHost.children("div"));b._spinButtonsContainer.attr("unselectable","on");b._spinButtonsContainer.addClass(b.toThemeProperty("jqx-fill-state-normal jqx-complex-input-child jqx-formatted-input-spin-buttons-container jqx-complex-input-spin-buttons-container"));if(b.rtl===false){b._spinButtonsContainer.addClass(b.toThemeProperty("jqx-complex-input-spin-buttons-container-ltr"))}else{b._spinButtonsContainer.addClass(b.toThemeProperty("jqx-complex-input-child-rtl jqx-complex-input-spin-buttons-container-rtl"))}var c='<div unselectable="on" class="'+b.toThemeProperty("jqx-fill-state-normal jqx-formatted-input-spin-button")+'"><div class="'+b.toThemeProperty("jqx-input-icon")+'"></div></div>';b._upbutton=a(c);b._spinButtonsContainer.append(b._upbutton);b._downbutton=a(c);b._spinButtonsContainer.append(b._downbutton);b._upArrow=b._upbutton.find("div");b._upArrow.addClass(b.toThemeProperty("jqx-icon-arrow-up"));b._downArrow=b._downbutton.find("div");b._downArrow.addClass(b.toThemeProperty("jqx-icon-arrow-down"));b._upArrow.add(b._downArrow).attr("unselectable","on");if(b.template){b._upbutton.addClass(b.toThemeProperty("jqx-"+b.template));b._downbutton.addClass(b.toThemeProperty("jqx-"+b.template))}},_addClasses:function(){var b=this;b.host.addClass(b.toThemeProperty("jqx-widget jqx-input jqx-complex-input jqx-widget-content"));if(b.baseHost){b.baseHost.addClass(b.toThemeProperty("jqx-widget jqx-complex-input-parent"));b.host.addClass(b.toThemeProperty("jqx-complex-input-child"))}if(b.roundedCorners===true){if(b._spinButtonsContainer){if(b.rtl===false){b.host.addClass(b.toThemeProperty("jqx-rc-l"));b._spinButtonsContainer.addClass(b.toThemeProperty("jqx-rc-r"))}else{b.host.addClass(b.toThemeProperty("jqx-rc-r"));b._spinButtonsContainer.addClass(b.toThemeProperty("jqx-rc-l"))}}else{b.host.addClass(b.toThemeProperty("jqx-rc-all"))}}if(b.disabled===true){b.host.attr("disabled",true);b.host.addClass(b.toThemeProperty("jqx-fill-state-disabled jqx-input-disabled"));if(b._spinButtonsContainer){b._spinButtonsContainer.addClass(b.toThemeProperty("jqx-fill-state-disabled"))}}if(b.rtl===true){b.host.add(b._spinButtonsContainer).addClass(b.toThemeProperty("jqx-complex-input-child-rtl"))}},_refreshPlaceHolder:function(c){var b=this;if("placeholder" in b.element){b.host.attr("placeHolder",b.placeHolder)}else{if(b.element.value===""||b.element.value===c){b.element.value=b.placeHolder}}},_setSize:function(){var d=this;function b(){var h=d.baseHost.height();var e=parseInt(d.host.css("border-left-width"),10)+parseInt(d.host.css("border-right-width"),10)+parseInt(d.host.css("padding-left"),10)+parseInt(d.host.css("padding-right"),10);var f=0;if(a.jqx.browser.msie&&a.jqx.browser.version<8){f=e;d.host.height(d.baseHost.height()-(parseInt(d.host.css("border-top-width"),10)+parseInt(d.host.css("border-bottom-width"),10)+parseInt(d.host.css("padding-top"),10)+parseInt(d.host.css("padding-bottom"),10))*2)}if(d._spinButtonsContainer){var g=typeof d.width==="string"&&d.width.charAt(d.width.length-1)==="%"?1:0;d.host.width(d.baseHost.width()-e-d._spinButtonsContainer.outerWidth()-f-g);if(a.jqx.browser.msie&&a.jqx.browser.version<8){d._spinButtonsContainer.height(h-(parseInt(d._spinButtonsContainer.css("border-top-width"),10)+parseInt(d._spinButtonsContainer.css("border-bottom-width"),10)+parseInt(d._spinButtonsContainer.css("padding-top"),10)+parseInt(d._spinButtonsContainer.css("padding-bottom"),10))*2)}}else{d.host.width(d.baseHost.width()-e-f)}}if(d.baseHost){d.baseHost.width(d.width);d.baseHost.height(d.height);b()}else{d.host.width(d.width);d.host.height(d.height)}if(a.jqx.browser.msie&&a.jqx.browser.version<9){d.host.css("line-height",d.host.height()+"px")}var c=d.baseHost||d.host;a.jqx.utilities.resize(c,function(){b();if((a.jqx.browser.msie&&a.jqx.browser.version<9||!a.jqx.browser.msie)&&typeof d.height==="string"&&d.height.charAt(d.height.length-1)==="%"){d.host.css("line-height",d.host.height()+"px")}})},_addHandlers:function(){var d=this,e;if(d.baseHost){e=d.baseHost[0].id}else{e=d.element.id}var b=[8,9,13,32,35,36,37,38,39,40,46];d.addHandler(d.host,"focus.jqxComplexInput"+e,function(){d.host.addClass(d.toThemeProperty("jqx-fill-state-focus"));if(d._spinButtonsContainer){d._spinButtonsContainer.addClass(d.toThemeProperty("jqx-fill-state-focus"))}if(d.bar){d.bar.addClass("focused")}if(d.label){d.label.addClass("focused")}if(!("placeholder" in d.element)&&(d.element.value===d.placeHolder)){d.element.value=""}if(d.decimalNotation!=="default"){var f=d._getCaretPosition();d.element.value=d._currentNumber.value;d._setCaretPosition(f)}});d.addHandler(d.host,"blur.jqxComplexInput"+e,function(){d.host.removeClass(d.toThemeProperty("jqx-fill-state-focus"));if(d._spinButtonsContainer){d._spinButtonsContainer.removeClass(d.toThemeProperty("jqx-fill-state-focus"))}if(d.bar){d.bar.removeClass("focused")}if(d.label){d.label.removeClass("focused")}if(d.element.value!==d.value||(("placeholder" in d.element)||(!("placeholder" in d.element)&&d.element.value===""))){d._onChange(d.value)}if(!("placeholder" in d.element)&&(d.element.value===""||d.element.value===d.placeHolder)){d.element.value=d.placeHolder}if(d.decimalNotation!=="default"){d._setNotation()}});d.addHandler(d.host,"keydown.jqxComplexInput"+e,function(h){var i=!h.charCode?h.which:h.charCode;d.changeType="keyboard";if(h.ctrlKey===true&&(i===67||i===86||i===88)){return}var g=String.fromCharCode(i);if(i>=96&&i<=105){g=(i-96).toString();i=i-48}if((!d._firefox&&i===187||d._firefox&&i===61)&&h.shiftKey===true){g="+"}else{if((!d._firefox&&i===189||d._firefox&&i===173)&&h.shiftKey===false){g="-"}else{if(i===190&&h.shiftKey===false){g="."}}}var k=d._allowedCharacters.test(g);if(k===true){if(g==="+"||g==="-"){var f=(d.element.value.match(/-/g)||[]).length+(d.element.value.match(/\+/g)||[]).length;if(f>1){return false}}else{if(g==="."){var j=(d.element.value.match(/\./g)||[]).length;if(j>1){return false}}else{if(g.toLowerCase()==="i"){if(d.element.value.indexOf(g.toLowerCase())!==-1){return false}}}}}else{if(b.indexOf(i)!==-1){return}else{return false}}});d.addHandler(d.host,"keypress.jqxComplexInput"+e,function(f){var g=!f.charCode?f.which:f.charCode;if(g===13){if(d.element.value!==d.value){d._onChange(d.value)}}});if(d._spinButtonsContainer){var c=d._upbutton.add(d._downbutton);d.addHandler(d._upbutton,"mousedown.jqxComplexInputSpinButtonUp"+e,function(){if(!d.disabled&&d.value!==""&&d.value!==null){d._upbutton.addClass(d.toThemeProperty("jqx-fill-state-pressed"));d.changeType="mouse";d._incrementOrDecrement(true)}});d.addHandler(d._upbutton,"mouseup.jqxComplexInputSpinButtonUp"+e,function(){if(!d.disabled&&d.value!==""&&d.value!==null){d._upbutton.removeClass(d.toThemeProperty("jqx-fill-state-pressed"))}});d.addHandler(d._downbutton,"mousedown.jqxComplexInputSpinButtonDown"+e,function(){if(!d.disabled&&d.value!==""&&d.value!==null){d._downbutton.addClass(d.toThemeProperty("jqx-fill-state-pressed"));d.changeType="mouse";d._incrementOrDecrement(false)}});d.addHandler(d._downbutton,"mouseup.jqxComplexInputSpinButtonDown"+e,function(){if(!d.disabled&&d.value!==""&&d.value!==null){d._downbutton.removeClass(d.toThemeProperty("jqx-fill-state-pressed"))}});d.addHandler(c,"mouseenter.jqxComplexInputSpinButtons"+e,function(g){if(!d.disabled&&d.value!==""&&d.value!==null){var f=a(g.target);if(f.hasClass("jqx-icon-arrow-up")||f.children().hasClass("jqx-icon-arrow-up")){d._upbutton.addClass(d.toThemeProperty("jqx-fill-state-hover"));d._upArrow.addClass(d.toThemeProperty("jqx-icon-arrow-up-hover"))}else{d._downbutton.addClass(d.toThemeProperty("jqx-fill-state-hover"));d._downArrow.addClass(d.toThemeProperty("jqx-icon-arrow-down-hover"))}}});d.addHandler(c,"mouseleave.jqxComplexInputSpinButtons"+e,function(g){if(!d.disabled&&d.value!==""&&d.value!==null){var f=a(g.target);if(f.hasClass("jqx-icon-arrow-up")||f.children().hasClass("jqx-icon-arrow-up")){d._upbutton.removeClass(d.toThemeProperty("jqx-fill-state-hover"));d._upArrow.removeClass(d.toThemeProperty("jqx-icon-arrow-up-hover"))}else{d._downbutton.removeClass(d.toThemeProperty("jqx-fill-state-hover"));d._downArrow.removeClass(d.toThemeProperty("jqx-icon-arrow-down-hover"))}}});d.addHandler(a("body"),"mouseup.jqxComplexInputSpinButtons"+e,function(){d._upbutton.add(d._downbutton).removeClass(d.toThemeProperty("jqx-fill-state-pressed"))})}},_removeHandlers:function(){var c=this,d;if(c.baseHost){d=c.baseHost[0].id}else{d=c.element.id}c.removeHandler(c.host,"focus.jqxComplexInput"+d);c.removeHandler(c.host,"blur.jqxComplexInput"+d);c.removeHandler(c.host,"keydown.jqxComplexInput"+d);c.removeHandler(c.host,"keypress.jqxComplexInput"+d);if(c._spinButtonsContainer){var b=c._upbutton.add(c._downbutton);c.removeHandler(c._upbutton,"mousedown.jqxComplexInputSpinButtonUp"+d);c.removeHandler(c._upbutton,"mouseup.jqxComplexInputSpinButtonUp"+d);c.removeHandler(c._downbutton,"mousedown.jqxComplexInputSpinButtonDown"+d);c.removeHandler(c._downbutton,"mouseup.jqxComplexInputSpinButtonDown"+d);c.removeHandler(b,"mouseenter.jqxComplexInputSpinButtons"+d);c.removeHandler(b,"mouseleave.jqxComplexInputSpinButtons"+d);c.removeHandler(a("body"),"mouseup.jqxComplexInputSpinButtons"+d)}},_onChange:function(c){var l=this,k,o;var n=l.element.value.toLowerCase();if(a.trim(n)!==""&&a.trim(n)!==l.placeHolder){if(n.indexOf("++")!==-1||n.indexOf("+-")!==-1){var f=n.indexOf("+");n=n.slice(0,f+1)+""+n.slice(f+2,n.length)}else{if(n.indexOf("--")!==-1||n.indexOf("-+")!==-1){var j=n.indexOf("-");n=n.slice(0,j+1)+""+n.slice(j+2,n.length)}}if(n.indexOf("..")!==-1){var d=n.indexOf(".");n=n.slice(0,d+1)+""+n.slice(d+2,n.length)}var m=l._getReal(n);var g=l._getImaginary(n);var b=" ";var e=g>=0?"+":"-";var h="i";k=m;o=g;if(isNaN(k)||isNaN(o)){l.element.value=c;return}l.element.value=m+""+b+""+e+""+b+""+Math.abs(g)+""+h;l.value=l.element.value}else{k=0;o=0;l.value=""}if(l.value!==c){l._currentNumber={value:l.value,realPart:k,imaginaryPart:o};l._raiseEvent("0",{value:l.value,oldValue:c,realPart:k,imaginaryPart:o})}},_incrementOrDecrement:function(j){var e=this,g,l,h=e.host.is(":focus"),k=e.element.value,i=e._currentNumber.realPart,d=e._currentNumber.imaginaryPart;if(h){g=e._getCaretPosition()}if(d>=0){l=k.indexOf("+")}else{if(k.charAt(0)==="-"){k=k.slice(1,k.length)}l=k.indexOf("-")}function f(o){var m=o.toString(),r=m.indexOf("."),q,p,n;if(r!==-1){p=parseInt(m.slice(0,r),10);n=m.slice(m.indexOf(".")+1);q="."}else{p=o;n="";q=""}if(j===true){o=p+e.spinButtonsStep}else{o=p-e.spinButtonsStep}o=parseFloat(o+""+q+""+n);return o}if(g===undefined||g<=l){i=f(i)}else{d=f(d)}var c=d>=0?"+":"-";var b=i+" "+c+" "+Math.abs(d)+"i";e.element.value=b;e._onChange(e.value);if(h){e._setCaretPosition(g)}else{if(e.decimalNotation!=="default"){e._setNotation()}}},_getCaretPosition:function(){var c=this.element;if("selectionStart" in c){return c.selectionStart}else{if(document.selection){c.focus();var d=document.selection.createRange();var b=document.selection.createRange().text.length;d.moveStart("character",-c.value.length);return d.text.length-b}}},_setCaretPosition:function(c){var b=this.element;setTimeout(function(){if("selectionStart" in b){b.focus();b.setSelectionRange(c,c)}else{var d=b.createTextRange();d.collapse(true);d.moveEnd("character",c);d.moveStart("character",c);d.select()}},10)},_exponentialToDecimal:function(h){var f=h.indexOf("e")+2;var e=h.slice(f);var b=e.indexOf("+");var g=e.indexOf("-");if(b!==-1&&(b<g||g===-1)){f=b}else{f=g}var d=e.slice(f);var i=h.replace(d,"");d=d.slice(0,d.length-1);var c=d.charAt(0);d=a.trim(d.slice(1));if(c==="-"){d="-"+d}i=parseFloat(i).toFixed(20)*1;d=parseFloat(d).toFixed(20)*1;return{realPart:i,imaginaryPart:d}},_setNotation:function(){var d=this;var e=d.getDecimalNotation(d._currentNumber.realPart,d.decimalNotation);var c=d.getDecimalNotation(Math.abs(d._currentNumber.imaginaryPart),d.decimalNotation);var b=d._currentNumber.imaginaryPart>=0?"+":"-";d.element.value=e+" "+b+" "+c+"i"},_toSuperScript:function(h,g){var f="-0123456789";var d="⁻⁰¹²³⁴⁵⁶⁷⁸⁹";var c="";for(var e=0;e<h.length;e++){if(g===true){var b=d.indexOf(h.charAt(e));c+=(b!==-1?f[b]:h[e])}else{var j=f.indexOf(h.charAt(e));c+=(j!==-1?d[j]:h[e])}}return c}})})(jqxBaseFramework);

