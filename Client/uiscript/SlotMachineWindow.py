#
# File: SlotMachineWindow.py
# Version: 1.0.0.0
# Author: Owsap
# Date: 2021.03.21
#

import app
import uiScriptLocale

BOARD_WIDTH = 225
BOARD_HEIGHT = 210

ROOT = "d:/ymir work/ui/game/slot_machine/"

window = {
	"name" : "SlotMachineWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "Board",
			"type" : "board",
			"style" : ("attach", "ltr"),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"children" :
			(
				## Title Bar
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 7,

					"width" : BOARD_WIDTH - 13,

					"children" :
					(
						## Title Bar Text
						{
							"name" : "TitleBarText",
							"type" : "text",

							"x" : 0,
							"y" : -2,

							"text" : uiScriptLocale.SLOT_MACHINE_TITLE,
							"all_align" : "center"
						},
					),
				},

				{
					## Board Container Image
					"name" : "BoardContainerBgImg",
					"type" : "image",
					"style" : ("attach",),

					"x" : 0,
					"y" : 32,

					"image" : ROOT + "inner_background.tga",
					"horizontal_align" : "center",

					"children" :
					(
						## Slot Machine Window
						{
							"name" : "SlotMachineWindow",
							"type" : "window",

							"x" : 0,
							"y" : 0,

							"width" : BOARD_WIDTH - 17,
							"height" : BOARD_HEIGHT - 40,

							"children" :
							(
								## Slot Machine Board Image
								{
									"name" : "SlotMachineBoardImage",
									"type" : "image",
									"style" : ("attach",),

									"x" : 0,
									"y" : 2,
									"horizontal_align" : "center",

									"image" : ROOT + "slot_machine_background.tga",

									"children" :
									(
										## Reel Icon Slots
										{
											"name" : "ReelIconSlot",
											"type" : "slot",

											"x" : 38,
											"y" : 31,

											"width" : 130,
											"height" : 32,

											"image" : "d:/ymir work/ui/public/Slot_Base.sub",

											"slot" : (
												{ "index" : 0, "x" : 0, "y" : 0, "width" : 32, "height" : 32 },
												{ "index" : 1, "x" : 50, "y" : 0, "width" : 32, "height" : 32 },
												{ "index" : 2, "x" : 100, "y" : 0, "width" : 32, "height" : 32 },
											),
										},
									),
								},

								## Betting Board Image
								{
									"name" : "BettingBoardImage",
									"type" : "image",
									"style" : ("attach",),

									"x" : 0,
									"y" : 74,

									"width" : 205,
									"height" : 51,

									"horizontal_align" : "center",
									"vertical_align" : "bottom",

									"image" : ROOT + "betting_background.tga",

									"children" :
									(
										## Bet Button
										{
											"name" : "BetButton",
											"type" : "button",

											"x" : 4,
											"y" : 3,

											"tooltip_text" : uiScriptLocale.SLOT_MACHINE_BET_TOOLTIP,
											"tooltip_x" : 0,
											"tooltip_y" : -20,

											"default_image" : ROOT + "play_button_default.tga",
											"over_image" : ROOT + "play_button_over.tga",
											"down_image" : ROOT + "play_button_down.tga",
										},

										## Betting Text
										{
											"name" : "BettingText",
											"type" : "text",

											"x" : 12,
											"y" : 5,

											"horizontal_align" : "center",
											"text_horizontal_align" : "center",

											"text" : uiScriptLocale.SLOT_MACHINE_BETTING_LABEL,
										},

										## Bet Input Board Image
										{
											"name" : "BetInputBoardImage",
											"type" : "image",
											"style" : ("attach",),

											"x" : 28,
											"y" : 27,

											"horizontal_align" : "center",
											"vertical_align" : "bottom",

											"image" : ROOT + "betting_slot.tga",

											"children" :
											(
												## Money Icon Image
												{
													"name" : "MoneyIconImg",
													"type" : "image",

													"x" : 4,
													"y" : 4,

													"image" : "d:/ymir work/ui/game/windows/money_icon.sub",
												},

												## Bet Value Edit Line
												{
													"name" : "BetValueEditLine",
													"type" : "editline",

													"x" : 45,
													"y" : 4,

													"horizontal_align" : "right",
													"text_horizontal_align" : "right",

													"width" : 0,
													"height" : 18,

													"input_limit" : 12,
													"only_number" : 1,

													"text" : "0",
												},

												## Decrease (Down) Bet Button
												{
													"name" : "DownBetButton",
													"type" : "button",

													"x" : 41,
													"y" : 3,

													"horizontal_align" : "center",
													"text_horizontal_align" : "center",

													"tooltip_text" : uiScriptLocale.SLOT_MACHINE_DOWN_BET_TOOLTIP,
													"tooltip_x" : 0,
													"tooltip_y" : -20,

													"default_image" : ROOT + "down_bet_default.tga",
													"over_image" : ROOT + "down_bet_over.tga",
													"down_image" : ROOT + "down_bet_default.tga",
												},

												## Increase (Up) Bet Button
												{
													"name" : "UpBetButton",
													"type" : "button",

													"x" : 57,
													"y" : 3,

													"horizontal_align" : "center",
													"text_horizontal_align" : "center",

													"tooltip_text" : uiScriptLocale.SLOT_MACHINE_UP_BET_TOOLTIP,
													"tooltip_x" : 0,
													"tooltip_y" : -20,

													"default_image" : ROOT + "up_bet_default.tga",
													"over_image" : ROOT + "up_bet_over.tga",
													"down_image" : ROOT + "up_bet_default.tga",
												},
											),
										},
									),
								},
							),
						},

						## Information (Jackpot) Window
						{
							"name" : "InformationWindow",
							"type" : "window",

							"x" : 0,
							"y" : 0,

							"width" : BOARD_WIDTH - 17,
							"height" : BOARD_HEIGHT - 40,

							"children" :
							(
								## Jackpot Board Image
								{
									"name" : "JackpotBoardImage",
									"type" : "image",
									"style" : ("attach",),

									"x" : 0,
									"y" : 0,
									"horizontal_align" : "center",
									"vertical_align" : "center",

									"image" : ROOT + "jackpots_background.tga",

									"children" :
									(
										## Jackpot Reel Icon Slots
										{
											"name" : "JackpotReelIconSlot",
											"type" : "slot",

											"x" : 60,
											"y" : 7,

											"width" : 130,
											"height" : 32,

											"image" : "d:/ymir work/ui/public/Slot_Base.sub",

											"slot" : (
												{ "index" : 0, "x" : 0, "y" : 0, "width" : 32, "height" : 32 },
												{ "index" : 1, "x" : 33, "y" : 0, "width" : 32, "height" : 32 },
												{ "index" : 2, "x" : 66, "y" : 0, "width" : 32, "height" : 32 },

												{ "index" : 3, "x" : 0, "y" : 33, "width" : 32, "height" : 32 },
												{ "index" : 4, "x" : 33, "y" : 33, "width" : 32, "height" : 32 },
												{ "index" : 5, "x" : 66, "y" : 33, "width" : 32, "height" : 32 },

												{ "index" : 6, "x" : 0, "y" : 66, "width" : 32, "height" : 32 },
												{ "index" : 7, "x" : 33, "y" : 66, "width" : 32, "height" : 32 },
												{ "index" : 8, "x" : 66, "y" : 66, "width" : 32, "height" : 32 },
											),
										},
									),
								},
							),
						},

						## Information (Jackpot) Button
						{
							"name" : "InformationButton",
							"type" : "toggle_button",

							"x" : 70,
							"y" : 22,

							"horizontal_align" : "center",
							"vertical_align" : "bottom",

							"tooltip_text" : uiScriptLocale.SLOT_MACHINE_INFORMATION_TOOLTIP,
							"tooltip_x" : 0,
							"tooltip_y" : -20,

							"default_image" : ROOT + "info_button_default.tga",
							"over_image" : ROOT + "info_button_over.tga",
							"down_image" : ROOT + "info_button_down.tga",
						},
					),
				},

				## Jackpot Reel Icon Effect (Animation Image)
				{
					"name" : "JackpotEffectAniImg",
					"type" : "ani_image",
					"style" : ("attach",),

					"x" : 50,
					"y" : 25,

					"delay" : 6,

					"images" :
					(
						ROOT + "effect/boom_eff1.sub",
						ROOT + "effect/boom_eff2.sub",
						ROOT + "effect/boom_eff3.sub",
						ROOT + "effect/boom_eff4.sub",
						ROOT + "effect/boom_eff5.sub",
						ROOT + "effect/boom_eff6.sub",
						ROOT + "effect/boom_eff7.sub",
						ROOT + "effect/boom_eff8.sub",
					),
				},

				## Reel Icon Effect 1 (Animation Image)
				{
					"name" : "ReelIconEffectAniImage1",
					"type" : "ani_image",
					"style" : ("attach",),

					"x" : 0,
					"y" : 25,

					"delay" : 6,

					"images" :
					(
						ROOT + "effect/boom_eff1.sub",
						ROOT + "effect/boom_eff2.sub",
						ROOT + "effect/boom_eff3.sub",
						ROOT + "effect/boom_eff4.sub",
						ROOT + "effect/boom_eff5.sub",
						ROOT + "effect/boom_eff6.sub",
						ROOT + "effect/boom_eff7.sub",
						ROOT + "effect/boom_eff8.sub",
					),
				},

				## Reel Icon Effect 2 (Animation Image)
				{
					"name" : "ReelIconEffectAniImage2",
					"type" : "ani_image",
					"style" : ("attach",),

					"x" : 50,
					"y" : 25,

					"delay" : 6,

					"images" :
					(
						ROOT + "effect/boom_eff1.sub",
						ROOT + "effect/boom_eff2.sub",
						ROOT + "effect/boom_eff3.sub",
						ROOT + "effect/boom_eff4.sub",
						ROOT + "effect/boom_eff5.sub",
						ROOT + "effect/boom_eff6.sub",
						ROOT + "effect/boom_eff7.sub",
						ROOT + "effect/boom_eff8.sub",
					),
				},

				## Reel Icon Effect 3 (Animation Image)
				{
					"name" : "ReelIconEffectAniImage3",
					"type" : "ani_image",
					"style" : ("attach",),

					"x" : 100,
					"y" : 25,

					"delay" : 6,

					"images" :
					(
						ROOT + "effect/boom_eff1.sub",
						ROOT + "effect/boom_eff2.sub",
						ROOT + "effect/boom_eff3.sub",
						ROOT + "effect/boom_eff4.sub",
						ROOT + "effect/boom_eff5.sub",
						ROOT + "effect/boom_eff6.sub",
						ROOT + "effect/boom_eff7.sub",
						ROOT + "effect/boom_eff8.sub",
					),
				},

				## Jackpot Success Effect (Animation Image)
				{
					"name" : "SuccessEffectAniImage",
					"type" : "ani_image",
					"style" : ("attach",),

					"x" : 30,
					"y" : 30,

					"delay" : 6,

					"images" :
					(
						ROOT + "effect/success_text_effect1.sub",
						ROOT + "effect/success_text_effect5.sub",
						ROOT + "effect/success_text_effect5.sub",
						ROOT + "effect/success_text_effect6.sub",
						ROOT + "effect/success_text_effect6.sub",
						ROOT + "effect/success_text_effect7.sub",
						ROOT + "effect/success_text_effect8.sub",
						ROOT + "effect/success_text_effect9.sub",
					),
				},

				# Help ToolTip Button
				{
					"name" : "HelpToolTipButton",
					"type" : "button",

					"x" : BOARD_WIDTH - 50,
					"y" : 7,

					"horizontal_align" : "left",

					"default_image" : ROOT + "question_mark_button_default.tga",
					"over_image" : ROOT + "question_mark_button_over.tga",
					"down_image" : ROOT + "question_mark_button_over.tga",
				},
			)
		},
	)
}
