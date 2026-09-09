package logic;

public class Client {
    private String id;
    private String name;

    public Client(String id, String name) throws Exception {
        if (id == null || id.equals(""))
            throw new Exception("El ID no puede estar vacio.");
        if (name == null || name.equals(""))
            throw new Exception("El nombre no puede estar vacio.");

        this.name = name;
        this.id = id;
        if (!isIdValid())
            throw new Exception("El ID no es valido");
    }




    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String toString() {
        return "Cliente(" + id + ", " + name + ")";
    }

    private boolean isIdValid() {
        for (char c : id.toCharArray()) {
            if (!isValidChar(c))
                return false;
        }
        return true;
    }

    private boolean isValidChar(char c){
        return c=='1' || c=='2' || c=='3' || c=='4' || c=='5' || c=='6' || c=='7' || c=='8' || c=='9' || c=='0' || c=='-';
    }
}
