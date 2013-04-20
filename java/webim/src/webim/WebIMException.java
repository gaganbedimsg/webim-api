package webim;

@SuppressWarnings("serial")
public class WebIMException extends Exception {

	private int code;
	
	public WebIMException(int code, String status) {
		super(status);
		this.code = code;
	}

	public int getCode() {
		return code;
	}

}
