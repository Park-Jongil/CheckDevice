/// HTTP Client 예제
/// REST API 를 사용하여 호출하는 예제.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System;
using System.Net.Http;
using System.Web;
using System.Net;
using System.IO;

namespace ConsoleProgram
{
    public class Class1
    {
        private const string URL = "https://sub.domain.com/objects.json?api_key=123";
        private const string DATA = @"{""object"":{""name"":""Name""}}";

        static void Main(string[] args)
        {
            Class1.CreateObject();
        }

        private static void CreateObject()
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(URL);
            request.Method = "POST";
            request.ContentType = "application/json"; 
            request.ContentLength = DATA.Length;
            StreamWriter requestWriter = new StreamWriter(request.GetRequestStream(), System.Text.Encoding.ASCII);
            requestWriter.Write(DATA);
            requestWriter.Close();

             try {
                WebResponse webResponse = request.GetResponse();
                Stream webStream = webResponse.GetResponseStream();
                StreamReader responseReader = new StreamReader(webStream);
                string response = responseReader.ReadToEnd();
                Console.Out.WriteLine(response);
                responseReader.Close();
            } catch (Exception e) {
                Console.Out.WriteLine("-----------------");
                Console.Out.WriteLine(e.Message);
            }

        }
    }
}

