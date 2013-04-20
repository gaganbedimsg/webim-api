package webim;

import java.util.Map;

public class Presence {

	private String show;
	
	private String status;
	
	public Presence(String show, String status) {
		this.show = show;
		this.status = status;
	}

	public void feed(Map<String, String> data) {
		data.put("show", show);
		data.put("status", status);
	}

}
