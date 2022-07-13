package com.silence.jtool

/**
 * process java class bytes convert to {@link JCFContent}
 */
trait JByteProcessor {
  def process(bytes: Array[Byte]) : JCFContent

  def preProcess(bytes: Array[Byte]) : String
}

object JByteProcessor {
  class JByteProcessorImpl extends JByteProcessor {
    override def process(bytes: Array[Byte]): JCFContent = ???

    override def preProcess(bytes: Array[Byte]): String = ???
  }
}

