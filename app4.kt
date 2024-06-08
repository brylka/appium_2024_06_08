package com.example.myapplication

import android.os.Build
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.annotation.RequiresApi
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.tooling.preview.Preview
import com.example.myapplication.ui.theme.MyApplicationTheme
import java.time.LocalTime
import java.time.format.DateTimeFormatter

class MainActivity : ComponentActivity() {
    @RequiresApi(Build.VERSION_CODES.O)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MyApplicationTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    MainScreen()
                }
            }
        }
    }
}

@RequiresApi(Build.VERSION_CODES.O)
@Composable
fun MainScreen() {
    var currentDate by remember { mutableStateOf("") }
    var currentTime by remember { mutableStateOf("") }
    Column {
        Greeting("Android")
        SimpleButton(onDateUpdate = { currentDate = it })
        TimeButton(onTimeUpdate = { currentTime = it })

        if (currentDate.isNotEmpty()) {
            Text("Aktualna data: $currentDate")
        }
        if (currentTime.isNotEmpty()) {
            Text("Aktualna godzina: $currentTime")
        }
    }
}

@Composable
fun Greeting(name: String) {
    Text(text = "Hello $name!")
}

@RequiresApi(Build.VERSION_CODES.O)
@Composable
fun SimpleButton(onDateUpdate: (String) -> Unit) {
    Button(
        onClick = { onDateUpdate(java.time.LocalDate.now().toString()) },
        modifier = Modifier.semantics { contentDescription = "Prosty Przycisk" }
    ) {
        Text("Pokaż datę")
    }
}

@RequiresApi(Build.VERSION_CODES.O)
@Composable
fun TimeButton(onTimeUpdate: (String) -> Unit) {
    Button(
        onClick = { onTimeUpdate(LocalTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss"))) },
        modifier = Modifier.semantics { contentDescription = "Przycisk Godziny" }
    ) {
        Text("Pokaż godzinę")
    }
}

@RequiresApi(Build.VERSION_CODES.O)
@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    MyApplicationTheme {
        MainScreen()
    }
}
