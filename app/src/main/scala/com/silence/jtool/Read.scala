package com.silence.jtool

import scala.io.Source


object Read {
  def read(file: String): Unit = {
    val source = Source.fromFile(file)
  }

}