/**
  * Created by Janwee on 2018/7/23.
  */
object spark{
  def main(args: Array[String]): Unit = {
    var temp=List(29,30,32,28,30,28,32)
    for (i<-Range(0,7)){
      if(i!=3) {
        println(temp(i))
      }
      else{println("周%s温度是：".format(i)+temp(i))}
    }
  }
}