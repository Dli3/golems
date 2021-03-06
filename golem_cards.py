'''
There are 36 golems in the game. 
Each golem has their own requirements to capture them.
Each golem have their own unique scores. 
'''

golems_cards = {'golem_1': {'points': 6,
                            'yellow': -2,
                            'green': -2,
                            'blue': 0,
                            'pink': 0,
                            'copper_coins': 0,
                            'silver_coins': 0
                            },

                'golem_2': {'points': 16,
                            'yellow': 0,
                            'green': 0,
                            'blue': 0,
                            'pink': -4,
                            'copper_coins': 0,
                            'silver_coins': 0
                            },

                'golem_3': {'points': 20,
                            'yellow': -1,
                            'green': -1,
                            'blue': -1,
                            'pink': -3,
                            'copper_coins': 0,
                            'silver_coins': 0
                            },

                'golem_4': {'points': 12,
                            'yellow': -1,
                            'green': -1,
                            'blue': -1,
                            'pink': -1,
                            'copper_coins': 0,
                            'silver_coins': 0
                            },

                'golem_5': {'points': 10,
                            'yellow': -2,
                            'green': 0,
                            'blue': 0,
                            'pink': -2,
                            'copper_coins': 0,
                            'silver_coins': 0
                            },

                'golem_6': {'points': 12,
                            'yellow': 0,
                            'green': -2,
                            'blue': 0,
                            'pink': -2,
                            'copper_coins': 0,
                            'silver_coins': 0
                            },

                'golem_7': {'points': 19,
                            'yellow': 0,
                            'green': -2,
                            'blue': -2,
                            'pink': -2,
                            'copper_coins': 0,
                            'silver_coins': 0
                            },

                'golem_8': {'points': 14,
                            'yellow': 0,
                            'green': -3,
                            'blue': 0,
                            'pink': -2,
                            'copper_coins': 0,
                            'silver_coins': 0
                            },

                'golem_9': {'points': 17,
                            'yellow': 0,
                            'green': 0,
                            'blue': -3,
                            'pink': -2,
                            'copper_coins': 0,
                            'silver_coins': 0
                            },

                'golem_10': {'points': 18,
                             'yellow': -1,
                             'green': -1,
                             'blue': -3,
                             'pink': -1,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_11': {'points': 8,
                             'yellow': -2,
                             'green': -3,
                             'blue': 0,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_12': {'points': 16,
                             'yellow': 0,
                             'green': -2,
                             'blue': 0,
                             'pink': -3,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_13': {'points': 17,
                             'yellow': -2,
                             'green': 0,
                             'blue': -2,
                             'pink': -2,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_14': {'points': 13,
                             'yellow': 0,
                             'green': -2,
                             'blue': -3,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_15': {'points': 20,
                             'yellow': 0,
                             'green': 0,
                             'blue': 0,
                             'pink': -5,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_16': {'points': 12,
                             'yellow': 0,
                             'green': -2,
                             'blue': -1,
                             'pink': -1,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_17': {'points': 16,
                             'yellow': -1,
                             'green': -3,
                             'blue': -1,
                             'pink': -1,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_18': {'points': 8,
                             'yellow': -2,
                             'green': 0,
                             'blue': -2,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_19': {'points': 14,
                             'yellow': 0,
                             'green': 0,
                             'blue': -2,
                             'pink': -2,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_20': {'points': 10,
                             'yellow': 0,
                             'green': -2,
                             'blue': -2,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_21': {'points': 12,
                             'yellow': 0,
                             'green': -3,
                             'blue': -2,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_22': {'points': 12,
                             'yellow': 0,
                             'green': 0,
                             'blue': -4,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_23': {'points': 12,
                             'yellow': -1,
                             'green': 0,
                             'blue': -2,
                             'pink': -1,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },
                'golem_24': {'points': 8,
                             'yellow': 0,
                             'green': -4,
                             'blue': 0,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },
                'golem_25': {'points': 14,
                             'yellow': -3,
                             'green': -1,
                             'blue': -1,
                             'pink': -1,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_26': {'points': 13,
                             'yellow': -2,
                             'green': -2,
                             'blue': -2,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_27': {'points': 15,
                             'yellow': -2,
                             'green': -2,
                             'blue': 0,
                             'pink': -2,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_28': {'points': 11,
                             'yellow': -2,
                             'green': 0,
                             'blue': -3,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_29': {'points': 15,
                             'yellow': 0,
                             'green': 0,
                             'blue': -5,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_30': {'points': 14,
                             'yellow': -2,
                             'green': 0,
                             'blue': 0,
                             'pink': -3,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_31': {'points': 11,
                             'yellow': -3,
                             'green': 0,
                             'blue': 0,
                             'pink': -2,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_32': {'points': 18,
                             'yellow': 0,
                             'green': 0,
                             'blue': -2,
                             'pink': -3,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_33': {'points': 7,
                             'yellow': -3,
                             'green': -2,
                             'blue': 0,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_34': {'points': 9,
                             'yellow': -2,
                             'green': -1,
                             'blue': 0,
                             'pink': -1,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_35': {'points': 9,
                             'yellow': -3,
                             'green': 0,
                             'blue': -2,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             },

                'golem_36': {'points': 10,
                             'yellow': 0,
                             'green': 0,
                             'blue': -5,
                             'pink': 0,
                             'copper_coins': 0,
                             'silver_coins': 0
                             }
                }
