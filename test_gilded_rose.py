# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):

        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]

    def test_conjured_items_should_decrease_twice_as_fast(self):
        conjured_item = "Conjured Mana Cake"
        items = [Item(conjured_item, 3, 6), Item(conjured_item, 1, 10), Item(conjured_item, 0, 4)]
        gr = GildedRose(items)

        gr.update_quality()

        # Conjured items should degrade in quality twice as fast (i.e., quality should decrease by 2 per day)
        assert gr.items == [Item(conjured_item, 2, 4), Item(conjured_item, 0, 8), Item(conjured_item, -1, 2)]


    def test_item_should_decrease_twice_as_fast_after_expiration(self):
        normal_item = "Elixir of the Mongoose"
        items = [Item(normal_item, 0, 7), Item(normal_item, -1, 10), Item(normal_item, -5, 20)]
        gr = GildedRose(items)

        gr.update_quality()

        # After sell_in reaches 0 or below, quality should decrease by 2 per day
        assert gr.items == [Item(normal_item, -1, 5), Item(normal_item, -2, 8), Item(normal_item, -6, 18)]


    def test_sulfuras_should_not_change(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]
        gr = GildedRose(items)

        gr.update_quality()

        # Sulfuras should remain unchanged
        assert gr.items == [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]


if __name__ == '__main__':
    unittest.main()
