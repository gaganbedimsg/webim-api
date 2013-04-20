package webim;

import org.json.JSONObject;

public class User {

	public String status;
	public String id;
	public String nick;
	public String show;

	public User(String id, String nick, String show, String status) {
		this.id = id;
		this.nick = nick;
		this.show = show;
		this.status = status;
	}

	public JSONObject toJson() {
		JSONObject json = new JSONObject();
		json.put("id", id);
		json.put("nick", nick);
		json.put("show", show);
		json.put("status", status);
		return json;
	}

}
