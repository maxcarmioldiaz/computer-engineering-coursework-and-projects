package logic;


public class Ticket {
    private int code;
    private String clientId;
    private static int consecutive = 100;

    public Ticket(String clientId) throws Exception {
        this.code = consecutive++;
        this.clientId = clientId;
        if (!isIdValid())
            throw new Exception("El ID no es valido.");
    }

    public String toString() {
        return "Tiquete(" + code + ", " + clientId + ")";
    }

    private boolean isIdValid() {
        for (char c : clientId.toCharArray()) {
            if (!isValidChar(c))
                return false;
        }
        return true;
    }

    private boolean isValidChar(char c){
        return c=='1' || c=='2' || c=='3' || c=='4' || c=='5' || c=='6' || c=='7' || c=='8' || c=='9' || c== '0' || c=='-';
    }
}
