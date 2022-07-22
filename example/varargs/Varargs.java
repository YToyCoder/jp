
public class Varargs {

  public static void main(String[] args) {
    varargsFn(0);
    varargsFn(1, "1");
    varargsFn(2, "1", "2");
  }

  public static varargsFn(int i, String ...str){
  }
}