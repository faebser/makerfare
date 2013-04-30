var ms = (function ($) {
	// javascript module pattern
	"use strict"; // enable strict mode for javascript module
	// private vars
	var module = {},
	blocks = null,
	classes = {
		inactive : "inactive",
		clickable : "clickable"
	}
	// private methods
	// public methods
	module.init = function () {
		blocks = $(".block");
		blocks.addClass(classes.inactive);
		blocks.addClass(classes.clickable);
		blocks.click(function () {
			$(this).toggleClass(classes.inactive);
		});
	};
	//return the module
	return module;
}($));

$(document).ready(function() {
	ms.init();
});