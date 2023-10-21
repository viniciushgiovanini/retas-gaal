import 'package:math_expressions/math_expressions.dart';
import 'package:test/test.dart';

void main() {
  test('equecao vetorial das retas', () {
    final ponto = Vector([Number(3), Number(2), Number(1)]);
    final vetor = Vector([Number(8), Number(9), Number(0)]);

    expect(
      (ponto + Variable('t') * vetor).toString(),
      '([3.0, 2.0, 1.0] + (t * [8.0, 9.0, 0.0]))',
    );
  });

  test('equacao parametrica', () {
    final ponto = Vector([Number(3), Number(2), Number(1)]);
    final vetor = Vector([Number(8), Number(9), Number(0)]);

    expect(
      (ponto + Variable('t') * vetor).toString(),
      '([3.0, 2.0, 1.0] + (t * [8.0, 9.0, 0.0]))',
    );
  });
}

// r1 = (x0 , y0, z0) vetor_r1 = (a, b, c)
// r2 = (x1 , y1, z1) vetor_r2 = (d, e, f)

// MOSTRAR ISSO PARA ELA:
// equacao vetorial das retas
// (x, y, z) = (x0, y0, z0) + h * (a, b, c)
// (x, y, z) = (x1, y1, z1) + t * (d, e, f)

// equacao parametrica das retas
// r1 ->
// x = x0 + at
// y = y0 + bt
// z = z0 + ct

// r2 ->
// x = x1 + dt
// y = y1 + et
// z = z1 + ft

// MOSTRAR SE AS RETAS SÃO X:
// - PARALELAS: a/d = b/e = c/f
//    - DISTINTAS: Caso o ponto_r1 não esteja em ponto_r2
//    - COINCIDENTES: Caso o ponto_r1 esteja em ponto_r2
//       - Calcular t1, t2, t3:
//         - t1 = (x0 - x1) / d
//         - t2 = (y0 - y1) / d
//         - t3 = (z0 - z1) / d
//         - Se t1 = t2 = t3: São coincidentes, caso contrário distintas.

// - CONCORRENTES:
//    - Utiliza o X e Y das retas:
//      - Sistema 1:
//        - x = x0 + ah
//        - x = x1 + dt
//          - Com isso: 1) ah - dt = x1 - x0
//       - Sistema 2:
//        - y = y0 + bh
//        - y = y1 + et
//          - Com isso: 2) bh - et = y1 - y0
//       - Resolver o último sistema:
//         - ah - dt = x1 - x0
//         - bh - et = y1 - y0
//       - Achar o valor de h e t:
//       - Achar valor de z:
//         - z_result1 = z0 + ch
//         - z_result2 = z1 + ft
//       - Se z_result1 = z_result2 são concorrentes então:
//       - Calcule o ângulo: angulo = cos^(-1) (abs( u * v))) / (abs(vet(u)) * abs(vet(v)))

// - REVERSAS: Se der falso para concorrentes ou paralelas.