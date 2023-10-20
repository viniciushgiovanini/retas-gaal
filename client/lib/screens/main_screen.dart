import 'package:flutter/material.dart';

class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  static const route = '/';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Retas Gaal')),
      // TODO: fix
      body: const Text('Lorem ipsum.'),
    );
  }
}
