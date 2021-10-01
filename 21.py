
from random import shuffle
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2,  "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
          "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # пустая колода
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0  # начинаем с нулевого значения
        self.aces = 0  # атрибут для отслеживания тузов

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # значенение по умолчанию или может быть установленно пользователем
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('Сколько фишек вы хотите поставить? '))
        except ValueError:
            print('Извините, ставка должна быть целым числом!')
        else:
            if chips.bet > chips.total:
                print("К сожалению, ваша ставка не может превышать", chips.total)
            else:
                break

def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Хотите походить или остановиться? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Игрок пас.Дилерр играет")
            playing = False

        else:
            print("Извините, пожалуйста, попробуйте еще раз.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Игрок банкрот!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Игрок выиграл")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Диллер банкрот")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Диллер !выиграл")
    chips.lose_bet()


def push(player, dealer):
    print("Дилер и игрок вничью!.")


while True:
    print('Добро пожаловать в BlackJack! ')

    # Создаем и перетасуем колоду, раздайте ем две карты каждому игроку
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # настройка фишек
    player_chips = Chips()  # значение по-умолчанию 100

    # Предложение сделать ставку
    take_bet(player_chips)

    # показ карт,но одна карта диллера скрыта
    show_some(player_hand, dealer_hand)