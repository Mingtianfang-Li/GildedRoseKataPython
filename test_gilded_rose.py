# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # for default test, change fixme to foo
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    #Example test
    def test_vest_item_should_decrease_after_one_day(self):

        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]

    # Aged Brie
    def test_aged_brie_should_increase_in_quality(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, 10, 30), Item(brie, 5, 48)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items == [Item(brie, 1, 1), Item(brie, 9, 31), Item(brie, 4, 49)]

    # Backstage passes
    def test_backstage_passes_should_increase_in_quality_and_drop_to_zero(self):
        passes = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(passes, 15, 20), Item(passes, 10, 49), Item(passes, 5, 49), Item(passes, 0, 20)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items == [Item(passes, 14, 21), Item(passes, 9, 50), Item(passes, 4, 50), Item(passes, -1, 0)]


    # Sulfuras
    def test_sulfuras_should_not_change(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items == [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]


if __name__ == '__main__':
    unittest.main()
