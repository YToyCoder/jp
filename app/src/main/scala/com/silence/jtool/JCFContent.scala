package com.silence.jtool

/**
 * java class file content
 */
trait JCFContent {
  def mainVersion():String
  def subVersion() : String
  def constPoolSize() : Int
  def constPool() : Array[String]
  def accessFlag() : String
}

object JCFContent {
  class JCFContentImpl extends JCFContent {
    override def mainVersion(): String = ???

    override def subVersion(): String = ???

    override def constPoolSize(): Int = ???

    override def constPool(): Array[String] = ???

    override def accessFlag(): String = ???
  }
}
