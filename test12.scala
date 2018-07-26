/**
  * Created by Janwee on 2018/7/25.
  */
object YaSparkTaobao{
  def main(args: Array[String]) {
    import org.json.JSONObject
    import org.apache.spark.{SparkContext,SparkConf}
    import scala.collection.mutable.ListBuffer
    val conf = new SparkConf().setMaster("local").setAppName("qunzi")
    val sc = new SparkContext(conf)
    val resultlist = sc.textFile("F:\\QQFileRecv\\1377860780\\FileRecv\\南京-厦门（合）\\南京-厦门（合）.txt")
      .filter(line=>{
        val isJson = line.startsWith("{\"")&&line.endsWith("}")
        //我们获取itemlist里面的status 如何为hide ，则直接过滤
        var isShow = false
        if(isJson){
          val json = new JSONObject(line)
          val status=json.getJSONObject("mods").getJSONObject("itemlist").getString("status")
          isShow = status.equals("show")//是否是show的数据
        }
        isJson&isShow
      })
      .flatMap(line=>{
        val json = new JSONObject(line)
        val goods=json.getJSONObject("mods").getJSONObject("itemlist").
          getJSONObject("data").getJSONArray("auctions")
        var list = ListBuffer[JSONObject]()
        //将jsonarray转换为scala支持的列表
        for(i<-0 to goods.length()-1){
          list.append(goods.getJSONObject(i))
        }
        list
      })
      .map(line=>{
        val view_price = line.getString("view_price").toFloat
        var price_name = ""
        if(view_price>=8000){
          price_name = "8000元以上"
        }else if(view_price>=5000){
          price_name = "5000~8000元"
        }else if(view_price>=3000){
          price_name = "3000~5000元"
        }else if(view_price>=1000){
          price_name = "1000~3000元"
        }else{
          price_name = "1000元以下"
        }
        var view_sales = 0
        try{
          view_sales = line.getString("view_sales").replace("人付款","").toInt
        } catch {
          case e:Exception=>{println("付款为零")}
        }
        (price_name,view_sales)//价格区间， 购买人数
      })
      .reduceByKey(_+_)
      .take(5)
    for(i<-resultlist){
      println(i)
    }
    sc.stop()
  }
}

