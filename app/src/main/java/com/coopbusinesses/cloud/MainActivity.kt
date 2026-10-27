package com.coopbusinesses.cloud

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val textView = TextView(this)
        textView.text = "Welcome to Coop App\nInstalled to SD Card Ready!"
        textView.textSize = 20f
        textView.setPadding(50, 200, 50, 50)
        setContentView(textView)
    }
}