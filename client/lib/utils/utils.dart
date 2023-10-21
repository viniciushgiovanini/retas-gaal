import 'package:math_expressions/math_expressions.dart';

class Utils {
  static dynamic eval(Expression expression) {
    return expression.evaluate(EvaluationType.VECTOR, ContextModel());
  }
}
