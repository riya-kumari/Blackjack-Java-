import java.io.Console;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

//# BlackJack pseudocode
//# Dealer Cards
//# Player Cards
// Order of Suit : Diamonds, Spades, Clubs, Hearts
//# Methods
//#     Deal Cards - DealingCard() : Player deals a card, returns a card 
//#     Display Cards - DisplayCard() : Displays the suit and value of card
//#     Shuffle Cards - ShuffleDeck() : Shuffles the deck
//		InitializeCards() 
//#     Sum of Dealer Cards() : DealsersSum() 
//#     Sum of Player Cards() : PlayersSum()
//		InitializeDeck() -- helper method
//#     CompareSums() -- Compare the sums of card between the player and dealer
//#     If the card is greater than 21 then BUST
//#     If the card is less than 21 --> Option of Hit or Stay
//#     If players sum <21 and greater than dealer, then player wins
//#     If players sum < dealers sum then player loses

public class game {

	static List<Card> playersCards = new ArrayList<Card>();
	static List<Card> dealersCards = new ArrayList<Card>();
	static Card[] deckOfCards = new Card[52];
	static String[] deckArray = new String[4];
	private static String userName = "";
	private static String startingSequence = "Blackjack Console Version 1.0 "+ "\n"+" To Start type in your name. ";
	static int deckCount = 0;
	static String indent = "    ";
	static Boolean isPlaying = true;

	public static void main(String args[]) {

		
		while(isPlaying)
		{
			runSequence();
		}
		System.out.println("Thank You for Playing");

	}
	
	public static void runSequence()
	{
		System.out.println(startingSequence);
		Scanner userInput = new Scanner(System.in);
		userName = userInput.nextLine();
		game g = new game();
		g.initializeDeck();
		g.initializeCards();
		g.shuffleCards();
		deckCount=0;
		playersCards = new ArrayList<Card>();
		dealersCards = new ArrayList<Card>();
		line();
		System.out.println("What is the amount you are betting?");
		int dealingAmt = userInput.nextInt();
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// Auto-generated catch block
			e.printStackTrace();
		}

		playersCards.add(deckOfCards[deckCount]);
		deckCount++;
		playersCards.add(deckOfCards[deckCount]);
		deckCount++;
		dealersCards.add(deckOfCards[deckCount]);
		deckCount++;
		dealersCards.add(deckOfCards[deckCount]);
		deckCount++;
		line();
		System.out.println("Your cards : " );
		displayCards(playersCards);
		System.out.println("Your sum : " + displaySum(playersCards));
		
		System.out.println("\n" + "Dealer's cards : ");
		displayCards(dealersCards);
		System.out.println("Dealers sum : " + displaySum(dealersCards));
		line();
		System.out.println("\n"+"Hit or Stand" + "");
		
		Scanner util = new Scanner(System.in);
		String input = util.nextLine();
		
		if(input.equalsIgnoreCase("Hit"))
		{
			playersCards.add(deckOfCards[deckCount]);
			System.out.println("Your cards are : " + "\n" + indent);
			displayCards(playersCards);
			System.out.println("Your sum : " + displaySum(playersCards));
			line();
			
			if(displaySum(playersCards)>21)
			{
				System.out.println("You have exceeded 21 and thereby lost your "+dealingAmt+". However you can play again in the hopes of winning your money again or maybe even more.");
			}
			else if(displaySum(playersCards)>displaySum(dealersCards))
			{
				System.out.println("Congratulations!!! You have won.");
			}
		}
			else
				if(displaySum(playersCards)>displaySum(dealersCards))
				{
					System.out.println("Congratulations!!! You have won.");
				}
				else
					System.out.println("It is a tie. Nobody wins or loses.");
			
		System.out.println("If you would like to play again, type start, else type stop");
		if(util.nextLine().equalsIgnoreCase("start"))
		{
			game anotherOne = new game();
			 System.out.flush(); 		    
			line();
			line();
			line();
			runSequence();
		}
		else
			isPlaying=false;
			
		
	}
	public static void line()
	{
		System.out.println( "----------------------------------------------");
	}

	public void initializeDeck() {

		deckArray[0] = "Diamonds";
		deckArray[1] = "Spades";
		deckArray[2] = "Clubs";
		deckArray[3] = "Hearts";

	}

	
	public static void initializeCards() {
		int i = 0;
		for (int suit = 0; suit < 4; suit++) {
			for (int count = 0; count < 13; count++) {
				if (count < 9)
					deckOfCards[i] = new Card(count + 2, deckArray[suit]);
				else
					deckOfCards[i] = new Card(10, deckArray[suit]);
				i++;

			}
		}

	}

	public static void shuffleCards() {

		Random rand = new Random();

//		Traversing the deck
		for (int i = 51; i >= 0; i--) {
//			creating a random index to shuffle with

			int pos = rand.nextInt(i + 1);

//			Swap the cards
			Card temp = deckOfCards[i];

			deckOfCards[i] = deckOfCards[pos];
			deckOfCards[pos] = temp;

		}

	}
	
	public static int displaySum(List<Card> list)
	{
		int sum = 0;
		for(Card c: list)
		{
			sum+=c.getValue();
		}
		return sum;
	}

	public static void displayCards(List<Card> list) {
	
		

		for (Card c : list) {
			System.out.println(indent + c.toString());
			
		}

		
	}

}