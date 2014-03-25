public class Ratio {

protected int num;
protected int den;

	public static final Ratio ZERO = new Ratio();

	private Ratio() {
	this(0,1);
	}

	public Ratio(int num, int den) {
	this.num = num;
	this.den = den;

	}

	public boolean equals(Object object) {
		if (object == this) {
		return true;

		} else if (!(object instanceof Ratio)) {
		return false;

		}
	Ratio that = (Ratio)object;
	return (this.num*that.den == that.num*this.den);

	}

	public int getNum() {
	return num;

	}

	public int getDen() {
	return den;
	}

	public String toString() {
	return String.format("%d/%d",num,den);
	}

	public double value() {
	return (double)num/den;
	}




public static void main(String[] args) {

	Ratio x = new Ratio(22,7);
	System.out.println("x=" + x);
}

}
