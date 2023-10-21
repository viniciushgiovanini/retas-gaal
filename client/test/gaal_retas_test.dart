import 'package:math_expressions/math_expressions.dart';
import 'package:retas_gaal/utils/utils.dart';
import 'package:test/test.dart';

void main() {
  test('equação vetorial', () {
    final ponto = Vector([Number(3), Number(2), Number(1)]);
    final vetor = Vector([Number(8), Number(9), Number(0)]);

    final variavel = Variable('t');

    final res = ponto + variavel * vetor;

    expect(
      res.toString(),
      '([3.0, 2.0, 1.0] + (t * [8.0, 9.0, 0.0]))',
    );
  });

  test('equação paramétrica', () {
    final ponto = Vector([Number(3), Number(2), Number(1)]);
    final vetor = Vector([Number(8), Number(9), Number(0)]);

    final variavel = Variable('t');

    final sistema = Vector([
      ponto[0] + variavel * vetor[0],
      ponto[1] + variavel * vetor[1],
      ponto[2] + variavel * vetor[2],
    ]);

    expect(
      sistema.toString(),
      '[(3.0 + (t * 8.0)), (2.0 + (t * 9.0)), (1.0 + (t * 0.0))]',
    );
  });

  test('retas paralelas', () {
    final a = Vector([Number(8), Number(10), Number(12)]);
    final b = Vector([Number(4), Number(5), Number(6)]);

    final v0 = Utils.eval(a[0] / b[0]);
    final v1 = Utils.eval(a[1] / b[1]);
    final v2 = Utils.eval(a[2] / b[2]);

    final res = v0 == v1 && v1 == v2;

    expect(
      res,
      true,
    );
  });

  test('retas não paralelas', () {
    final a = Vector([Number(6), Number(10), Number(12)]);
    final b = Vector([Number(4), Number(5), Number(6)]);

    final v0 = Utils.eval(a[0] / b[0]);
    final v1 = Utils.eval(a[1] / b[1]);
    final v2 = Utils.eval(a[2] / b[2]);

    final res = v0 == v1 && v1 == v2;

    expect(
      res,
      false,
    );
  });

  test('retas coincidentes', () {
    final pontoR1 = Vector([Number(1), Number(2), Number(3)]); // (x0, y0, z0)
    final pontoR2 = Vector([Number(3), Number(4), Number(5)]); // (x1, y1, z1)
    final vetorR2 = Vector([Number(4), Number(4), Number(4)]); // (d, e, f)

    final v0 = Utils.eval((pontoR1[0] - pontoR2[0]) / vetorR2[0]);
    final v1 = Utils.eval((pontoR1[1] - pontoR2[1]) / vetorR2[1]);
    final v2 = Utils.eval((pontoR1[2] - pontoR2[2]) / vetorR2[2]);

    final res = v0 == v1 && v1 == v2;

    expect(
      res,
      true,
    );
  });

  test('retas distintas', () {
    final pontoR1 = Vector([Number(1), Number(2), Number(3)]); // (x0, y0, z0)
    final pontoR2 = Vector([Number(3), Number(4), Number(5)]); // (x1, y1, z1)
    final vetorR2 = Vector([Number(4), Number(4), Number(7)]); // (d, e, f)

    final v0 = Utils.eval((pontoR1[0] - pontoR2[0]) / vetorR2[0]);
    final v1 = Utils.eval((pontoR1[1] - pontoR2[1]) / vetorR2[1]);
    final v2 = Utils.eval((pontoR1[2] - pontoR2[2]) / vetorR2[2]);

    final res = v0 == v1 && v1 == v2;

    expect(
      res,
      false,
    );
  });

  test('retas concorrentes', () {
    final pontoR1 = Vector([Number(0), Number(0), Number(0)]); // (x0, y0, z0)
    final pontoR2 = Vector([Number(1), Number(1), Number(1)]); // (x1, y1, z1)
    final vetorR1 = Vector([Number(1), Number(1), Number(0)]); // (a, b, c)
    final vetorR2 = Vector([Number(0), Number(0), Number(-1)]); // (d, e, f)
    // final pontoR1 = Vector([Number(0), Number(0), Number(0)]); // (x0, y0, z0)
    // final pontoR2 = Vector([Number(1), Number(0), Number(0)]); // (x1, y1, z1)
    // final vetorR1 = Vector([Number(0), Number(5), Number(0)]); // (a, b, c)
    // final vetorR2 = Vector([Number(-1), Number(0), Number(0)]); // (d, e, f)
    // final pontoR1 = Vector([Number(3), Number(1), Number(2)]); // (x0, y0, z0)
    // final pontoR2 = Vector([Number(5), Number(-3), Number(4)]); // (x1, y1, z1)
    // final vetorR1 = Vector([Number(1), Number(2), Number(-1)]); // (a, b, c)
    // final vetorR2 = Vector([Number(3), Number(-2), Number(1)]); // (d, e, f)

    // final t = Variable('t');
    // final h = Variable('h');

    // Base:
    // (x0, y0, z0)
    // (x1, y1, z1)
    // (a, b, c)
    // (d, e, f)

    // Sistema para resolver:
    // ah - dt = x1 - x0
    // bh - et = y1 - y0

    // P = z0 + e * h
    // Q = z1 + f * t

    // ah - dt = x1 - x0
    // Wolf: h = (d * t - w - x) / a
    // Wolf: t = (x1 - x0 - a * h) / - d
    // bh - et = y1 - y0
    // Wolf: t = (b * h + y - z) / e
    // Wolf: h = (y1 - y0 + e * t) / b

    // wolf:
    // h = (d * ((b * h + y - z) / e) - w - x) / a
    // !!!!!!!!!!!!  h = (3 * ((2 * h + 1 - -3) / -2) - 5 - 3) / 1
    // !!!!!!!!!!!!  h = (3 * ((2 * h + 1 - -3) / -2) - 5 - 3) / 1
    // h = (d * (z - y) + e * (w + x)) / (b * d - e * a) and b * d != e * a and a != 0

    // t = (b * ((d * t - w - x) / a) + y - z) / e
    // t = (a * (z - y) + b * (w + x)) / (b * d - e * a) and b * d != e * a and a != 0

    // h = (d * (z - y) + e * (w + x)) / (b * d - e * a)
    // t = (a * (z - y) + b * (w + x)) / (b * d - e * a)

    // P = q + e * ((d * (z - y) + e * (w + x)) / (b * d - e * a))
    // P = 0 + 0 * ((-1 * (0 - 0) + 0 * (1 + 0)) / (1 * -1 - 0 * 0))
    // P = 0

    // Q = r + f * ((a * (z - y) + b * (w + x)) / (b * d - e * a))
    // Q = 0 + 0 * ((0 * (0 - 0) + 1 * (1 + 0)) / (1 * -1 - 0 * 0))
    // Q = 0

    // P = q + e * ((d * (z - y) + e * (w + x)) / (b * d - e * a))
    // P = 2 + -2 * ((3 * (-3 - 1) + -2 * (5 + 3)) / (2 * 3 - -2 * 1))
    // P = 9
    // Q = r + f * ((a * (z - y) + b * (w + x)) / (b * d - e * a))

    // Sure recente:
    // h = (x1 - x0 + dt) / a
    // t = (-y1 + y0 + bh) / e
    // h = (x1 - x0 + d * ((-y1 + y0 + b * h) / e)) / a
    // x1 = w
    // x0 = x
    // y1 = z
    // y0 = y
    // z0 = q
    // z1 = r

    // !!!!!! pode ta errado:
    // wolfram alpha:
    // h = (d * (z - y) + e * (x - w)) / (b * d - e * a)
    // t = (-z + y + b * ((d * (z - y) + e * (x - w)) / (b * d - e * a))) / e
    //
    // P = q + e * ((d * (z - y) + e * (x - w)) / (b * d - e * a))
    // Q = r + f * ((-z + y + b * ((d * (z - y) + e * (x - w)) / (b * d - e * a))) / e)
    // !!!!!!

    // exemplo:
    // p0 = (0, 0, 0)
    // p1 = (1, 0, 0)
    // v0 = (0, 1, 0)
    // v1 = (-1, 0, 0)

    // ((d * (z - y) + e * (w + x)) / (b * d - e * a))
    final h = ((vetorR2[0] * (pontoR2[1] - pontoR1[1]) +
            vetorR2[1] * (pontoR2[0] + pontoR1[0])) /
        (vetorR1[1] * vetorR2[0] - vetorR2[1] * vetorR1[0]));

    final t = ((vetorR1[0] * (pontoR2[1] - pontoR1[1]) +
            vetorR1[1] * (pontoR2[0] + pontoR1[0])) /
        (vetorR1[1] * vetorR2[0] - vetorR2[1] * vetorR1[0]));

    //// P = q + e * ((d * (z - y) + e * (w + x)) / (b * d - e * a))
    final p = pontoR1[2] + vetorR2[1] * h;

    //// Q = r + f * ((a * (z - y) + b * (w + x)) / (b * d - e * a))
    final q = pontoR2[2] + vetorR2[2] * t;

    print(
      'p: ${Utils.eval(p)}, q: ${Utils.eval(q)}, h: ${Utils.eval(h)}, t: ${Utils.eval(t)}',
    );

    final res = Utils.eval(p) == Utils.eval(q);

    // se for concorrente, ângulo e interseção

    expect(
      res,
      true,
    );
  });
}

// ponto_r1 = (x0 , y0, z0) vetor_r1 = (a, b, c)
// ponto_r2 = (x1 , y1, z1) vetor_r2 = (d, e, f)

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
//         - t2 = (y0 - y1) / e
//         - t3 = (z0 - z1) / f
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
//         - Após achar t substituir em um sistema da reta 1: valor de X, Y e Z = ponto de intersecção
//       - Achar valor de z:
//         - z_result1 = z0 + ch
//         - z_result2 = z1 + ft
//       - Se z_result1 = z_result2 são concorrentes então:
//       - Calcule o ângulo: angulo = cos^(-1) (abs( u * v))) / (abs(vet(u)) * abs(vet(v)))

// - REVERSAS: Se der falso para concorrentes ou paralelas.
