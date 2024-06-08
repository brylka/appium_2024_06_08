package com.example.myapplication

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.myapplication.ui.theme.MyApplicationTheme
import java.lang.Exception

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MyApplicationTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    CalculatorScreen()
                }
            }
        }
    }
}

@Composable
fun CalculatorScreen() {
    var expression by remember { mutableStateOf("") }
    var result by remember { mutableStateOf("") }

    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(text = expression, style = MaterialTheme.typography.headlineMedium)
        Text(text = "Wynik: $result", style = MaterialTheme.typography.bodyLarge)
        Spacer(modifier = Modifier.height(20.dp))

        val buttons = listOf(
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        )

        buttons.chunked(4).forEach { row ->
            Row {
                row.forEach { label ->
                    CalculatorButton(label) { input ->
                        when (input) {
                            "=" -> {
                                try {
                                    result = evaluateExpression(expression)
                                } catch (e: Exception) {
                                    result = "Błąd"
                                }
                            }
                            "C" -> {
                                expression = ""
                                result = ""
                            }
                            else -> {
                                expression += input
                            }
                        }
                    }
                }
            }
        }
    }
}

@Composable
fun CalculatorButton(label: String, onClick: (String) -> Unit) {
    Button(
        onClick = { onClick(label) },
        modifier = Modifier
            .semantics { contentDescription = "Przycisk $label" }
            .padding(4.dp)

    ) {
        Text(label)
    }
}

fun evaluateExpression(expression: String): String {
    if (expression.isBlank()) return ""

    val operators = setOf('+', '-', '*', '/')
    val numbers = mutableListOf<Double>()
    val operations = mutableListOf<Char>()

    var currentNumber = ""
    for (char in expression) {
        if (char in operators) {
            numbers.add(currentNumber.toDouble())
            currentNumber = ""
            operations.add(char)
        } else {
            currentNumber += char
        }
    }
    numbers.add(currentNumber.toDouble())

    while (operations.isNotEmpty()) {
        val op = operations.removeAt(0)
        val num1 = numbers.removeAt(0)
        val num2 = numbers.removeAt(0)

        val result = when (op) {
            '+' -> num1 + num2
            '-' -> num1 - num2
            '*' -> num1 * num2
            '/' -> if (num2 == 0.0) return "Błąd dzielenia przez 0" else num1 / num2
            else -> throw IllegalArgumentException("Nieznany operator: $op")
        }

        numbers.add(0, result)
    }

    return numbers.first().toString()
}


@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    MyApplicationTheme {
        CalculatorScreen()
    }
}
