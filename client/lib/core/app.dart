import 'package:flutter/material.dart';
import 'package:retas_gaal/screens/main_screen.dart';

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Retas Gaal',
      routes: {
        MainScreen.route: (context) => const MainScreen(),
      },
    );
  }
}
