package webim;

public class User {

	private String id;
	private String nick;

	public User(String id, String nick) {
		this.setId(id);
		this.setNick(nick);
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getNick() {
		return nick;
	}

	public void setNick(String nick) {
		this.nick = nick;
	}
}
