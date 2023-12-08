from Hand import Hand, HandType
import pytest


class TestHand:

    def test_type(self):
        assert Hand('AAAAA').type == HandType.FIVE_KIND
        assert Hand('AAAA2').type == HandType.FOUR_KIND
        assert Hand('AAA22').type == HandType.FULL_HOUSE
        assert Hand('AAA23').type == HandType.THREE_KIND
        assert Hand('AA223').type == HandType.TWO_PAIR
        assert Hand('AA234').type == HandType.ONE_PAIR

    def test_cards_valid(self):
        assert Hand.get_card_value('A')
        with pytest.raises(ValueError):
            assert Hand.get_card_value('Z')

    def test_winner(self):
        assert Hand.get_winner(Hand('AAAAA'), Hand('AAAA2')).cards == 'AAAAA'
        assert Hand.get_winner(Hand('AAAAA'), Hand('22222')).cards == 'AAAAA'
        assert Hand.get_winner(Hand('22222'), Hand('AAAAA')).cards == 'AAAAA'
        assert Hand.get_winner(Hand('AAA22'), Hand('AAA33')).cards == 'AAA33'
        assert Hand.get_winner(Hand('AKQJT'), Hand('AKQJ3')).cards == 'AKQJT'
        assert Hand.get_winner(Hand('AQ829'), Hand('AJ7AA')).cards == 'AJ7AA'
        assert Hand.get_winner(Hand('AKAAA'), Hand('AA3TJ')).cards == 'AKAAA'

        with pytest.raises(ValueError):
            assert Hand.get_winner(
                Hand('AAA32'), Hand('AAA32')).cards == 'AAA33'

    def test_bid(self):
        assert Hand('AAAAA', '10').bid == 10
        assert Hand('AAAAA', 10).bid == 10

    def test_hand_size(self):
        with pytest.raises(ValueError):
            assert Hand('A234')
            assert Hand('')
            assert Hand(None)
            assert Hand('A24567')

    def test_joker(self):
        assert Hand('AAAAJ', joker='J').joker == 'J'

    def test_joker_type(self):
        assert Hand('KTJJT', joker='T').type == HandType.FOUR_KIND
        assert Hand('QQQJA', joker='Q').type == HandType.FOUR_KIND
        assert Hand('T55J5', joker='5').type == HandType.FOUR_KIND
        assert Hand('AAAAJ', joker='J').type == HandType.FIVE_KIND
        assert Hand('AAA2J', joker='J').type == HandType.FOUR_KIND
        assert Hand('2345J', joker='J').type == HandType.ONE_PAIR
        assert Hand('2355J', joker='J').type == HandType.THREE_KIND

    def test_joker_winner(self):
        assert Hand.get_winner(Hand('J22A2', 1, 'J'), Hand(
            '2AAJA', 1, 'J')).cards == '2AAJA'
        assert Hand.get_winner(Hand('JJJJJ', 1, 'J'), Hand(
            '22222', 1, 'J')).cards == '22222'
