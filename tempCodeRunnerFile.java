public class CalcEngine {
    public static void main(String[] args) {
        try {
            String expression = args[0];
            double result = evaluate(expression);
            System.out.println(result);
        } catch (Exception e) {
            System.out.println("Error");
        }
    }

    public static double evaluate(String expr) {
        // Remove spaces
        expr = expr.replaceAll("\\s+", "");

        // Basic operators: + - * /
        double result = 0.0;
        char lastOp = '+';
        StringBuilder number = new StringBuilder();

        for (int i = 0; i < expr.length(); i++) {
            char ch = expr.charAt(i);

            if (Character.isDigit(ch) || ch == '.') {
                number.append(ch);
            }

            if (!Character.isDigit(ch) && ch != '.' || i == expr.length() - 1) {
                double num = Double.parseDouble(number.toString());
                number = new StringBuilder();

                switch (lastOp) {
                    case '+':
                        result += num;
                        break;
                    case '-':
                        result -= num;
                        break;
                    case '*':
                        result *= num;
                        break;
                    case '/':
                        result /= num;
                        break;
                }

                lastOp = ch;
            }
        }
        return result;
    }
}
