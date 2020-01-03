
public class Card {
	

	private int number = 0;
	private String type = "";
	
	
	public Card(int n, String t)
	{

		number = n;
		type = t;
	}
	

	/*
	 * I'm going to assume that a face card 
	 * Queen = 20
	 * King = 21
	 * Ace = 22
	 * Jack = 19
	 */
	public int getValue()
	{
		if(number>15 && number < 23)
		{
			
			return 10;
		}
		return number;
	}
	
	public String getSuit()
	{
		
		return type;
	}
	
	public String toString()
	{
		return this.getValue() + " , " + this.getSuit();
	}
	
}
