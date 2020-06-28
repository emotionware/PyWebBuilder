define("ace/snippets/vbscript",["require","exports","module"], function(require, exports, module) {
"use strict";

exports.snippetText ="# Prototype\n\

snippet test\n\
	${1:Test} \n\


";
exports.scope = "vbscript";

});                (function() {
                    window.require(["ace/snippets/vbscript"], function(m) {
                        if (typeof module == "object" && typeof exports == "object" && module) {
                            module.exports = m;
                        }
                    });
                })();
            