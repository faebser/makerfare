var ms = (function ($) {
	// javascript module pattern
	"use strict"; // enable strict mode for javascript module
	// private vars
	var module = {},
	blocks = $(".block").not(".simple"),
	slider = $("#sliderOuter #slider"),
	sliderElements = slider.find("li"),
	sliderElementWidth = null,
	sliderElementsAmount = null,
	sliderElementsMaxMargin = null,
	slideTime = 2000,
	sliderId = null,
	classes = {
		inactive : "inactive",
		clickable : "clickable",
		sliderReady : "sliderReady"
	};
	// private methods
	var clickHandlers = function () {
		blocks.find("h2").click(function () {
			$(this).parent().toggleClass(classes.inactive);
		});
		slider.hover(sliderPause, sliderContinue);
	},
	sliderNext = function () {
		var currentMargin = parseInt(slider.css("margin-left")),
		newMargin = null;
		if(currentMargin == sliderElementsMaxMargin || currentMargin >= sliderElementsMaxMargin) {
			newMargin = 0;
		}
		else {
			newMargin = currentMargin + sliderElementWidth * -1;
		}
		slider.css("margin-left", newMargin);
	},
	sliderPause = function () {
		window.clearInterval(sliderId);
	},
	sliderContinue = function () {
		sliderId = window.setInterval(sliderNext, slideTime);
	},
	sliderMath = function () {
		sliderElementsAmount = sliderElements.length;
		sliderElementWidth = sliderElements.first().outerWidth();
		sliderElementsMaxMargin = (sliderElementsAmount - 1) * sliderElementWidth * -1;
	};
	// public methods
	module.init = function () {
		blocks.addClass(classes.inactive + " " + classes.clickable);
		sliderMath();
		slider.parent().addClass(classes.sliderReady);
		clickHandlers();
		sliderContinue();
	};
	//return the module
	return module;
}($));

$(document).ready(function() {
	ms.init();
});