public class CalcEngine {

    public static void main(String[] args) {
        try {
            if (args.length == 0) {
                System.out.println("Error");
                return;
            }

            String expression = args[0];

            double result = evaluate(expression);
            System.out.println(result);

        } catch (Exception e) {
            System.out.println("Error");
        }
    }

    public static double evaluate(String expr) throws Exception {
        expr = expr.replaceAll("\\s+", "");

        if (!isValid(expr)) {
            throw new Exception("Invalid");
        }

        double result = 0.0;
        char lastOp = '+';
        StringBuilder number = new StringBuilder();

        for (int i = 0; i < expr.length(); i++) {
            char ch = expr.charAt(i);

            if (Character.isDigit(ch) || ch == '.') {
                number.append(ch);
            }

            // End of a number or operator
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
                        if (num == 0)
                            throw new Exception("DivideByZero");
                        result /= num;
                        break;
                }

                lastOp = ch;
            }
        }

        return result;
    }

    // Validation checks
    public static boolean isValid(String expr) {

        // No empty expression
        if (expr == null || expr.isEmpty())
            return false;

        // Cannot start with operator except minus
        if ("+*/.".indexOf(expr.charAt(0)) != -1)
            return false;

        // Cannot end with operator
        if ("+-*/.".indexOf(expr.charAt(expr.length() - 1)) != -1)
            return false;

        // Prevent two operators in a row
        if (expr.matches(".*[+\\-*/]{2,}.*"))
            return false;

        // Prevent multiple decimals in a number
        String[] parts = expr.split("[+\\-*/]");
        for (String p : parts) {
            if (p.chars().filter(c -> c == '.').count() > 1)
                return false;
        }

        return true;
    }
}
