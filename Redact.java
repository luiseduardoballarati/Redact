import java.util.ArrayList;

public class Redact {

    public static String redact(String content, String[] redactWords) {
        ArrayList<String> newRedactList = new ArrayList<>();

        for(String str : redactWords){
            newRedactList.add(str);
            }
        return " ";
    }
    public static void main(String[] args) {
        String content = "The quick brown fox jumps over the lazy dog!";
        String[] redactWords = {"Fox", "jumps", "dog"};

        String redactedContent = redact(content, redactWords);
        System.out.println("Redacted content: " + redactedContent);
        String[] stringSplitted = content.split(" ");
        System.out.println(stringSplitted);
    }
}
