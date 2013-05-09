var ms = (function ($) {
	// javascript module pattern
	"use strict"; // enable strict mode for javascript module
	// private vars
	var module = {},
	win = $(window),
	blocks = $(".block").not(".simple"),
	articles = $("article"),
	menu = $("#menuContainer"),
	menuOffset = menu.offset().top,
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
		sliderReady : "sliderReady",
		fixed : "fixed",
		even : "even",
		block : ".block"
	};
	// private methods
	var clickHandlers = function () {
		blocks.find("h2").click(function () {
			$(this).parent().toggleClass(classes.inactive);
		});
		slider.hover(sliderPause, sliderContinue);
		win.scroll(windowScrollTest);
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
	},
	windowScrollTest = function () {
		if(win.scrollTop() > menuOffset && !menu.hasClass(classes.fixed)) {
			menu.addClass(classes.fixed);
		}
		else if(win.scrollTop() <= menuOffset && menu.hasClass(classes.fixed)) {
			menu.removeClass(classes.fixed);
		}
	},
	blockCounter = function () {
		articles.each( function(index, element) {
			console.log("article: " + $(element).attr("id"));
			$(element).find(classes.block).each( function(index, element2) {
				var e = $(element2);
				console.log("index: " + e.index(classes.block));
				if(e.index() % 2 == 0) {
					e.addClass(classes.even);
				}
			});
		});
	};
	// public methods
	module.init = function () {
		blocks.addClass(classes.inactive + " " + classes.clickable);
		sliderMath();
		slider.parent().addClass(classes.sliderReady);
		clickHandlers();
		sliderContinue();
		blockCounter();
	};
	//return the module
	return module;
}($));

$(document).ready(function() {
	ms.init();
});