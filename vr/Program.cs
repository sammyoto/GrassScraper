using StereoKit;
using System;
using System.Net.Http;
using System.Text;
using Newtonsoft.Json;
using System.IO;
using System.Drawing;
using System.Drawing.Imaging;

namespace vrToApi
{
    internal class Program
    {
        // Class for the data needed to post to API
        public class Post { 
            public string handy { get; set; }
            public string stickX { get; set; }
            public string stickY { get; set; }
            public string trigger { get; set; }
            public string x1 { get; set; }
            public string x2 { get; set; }
        }


        // method to get images from AWS
        // Not-working, extremely slow, makes VR lag to the point where you can't control lawn mower
        // In need of faster streaming methods than downloading and cubemapping in real time on the machine
        static byte[] getImage()
        {
            string imgURL = "https://9f3low7kki.execute-api.us-west-2.amazonaws.com/v2/holewherejpglives-1?file=test20220707T091229.00006.jpg";
            HttpClient imgClient = new HttpClient();
            var data = imgClient.GetStringAsync(imgURL);
            var temp = Convert.FromBase64String(data.Result);
            return temp;
        }

        // method to send contoller data to API
        static void sendControls(Handed hand, Controller c)
        {
            // Initialize temp variables

            // The analog stick on the controller
            Vec2 temp = c.stick;

            HttpClient client = new HttpClient();
            string url = "https://wfevbii2w47dcqjn3tkwyf6evq0pbckw.lambda-url.us-west-2.on.aws/vrPost";

            // Initialize a post class with controller data
            var instructions = new Post() {
                handy = hand.ToString(),
                stickX = temp.x.ToString(),
                stickY = temp.y.ToString(),
                trigger = c.trigger.ToString(),
                x1 = c.x1.ToString(),
                x2 = c.x2.ToString()
            };

            // Serialize the object into JSON format
            var json = JsonConvert.SerializeObject(instructions);

            // Send the data to the endpoint
            var sentData = new StringContent(json, Encoding.UTF8, "application/json");
            client.PostAsync(url, sentData);
        }

        static void Main(string[] args)
        {
            // Initialize StereoKit
            SKSettings settings = new SKSettings
            {
                appName = "vrToApi",
                assetsFolder = "Assets",
            };
            if (!SK.Initialize(settings))
                Environment.Exit(1);
            

            // Core application loop

            int i = 0;
            while (SK.Step(() =>
            {
                // Define Controllers
                Controller leftController = Input.Controller(Handed.Left);
                Controller rightController = Input.Controller(Handed.Right);

                // Change camera position according to right stick
                Quat rotation = Renderer.CameraRoot.Pose.orientation;
                Matrix temp = Matrix.R(rightController.stick.y * 2, rightController.stick.x * 2, 0);
                Renderer.CameraRoot *= temp;

                //only send instructions certain ammount of times per second
                if (i == 0)
                {
                    sendControls(Handed.Left, leftController);
                }
                
                Renderer.SkyTex = Tex.FromCubemapEquirectangular("noah.jpg", out SphericalHarmonics lighting);

                i += 1;
                // make i larger or smaller depending on how many times you want the API to get posted to per second
                if (i >= 14){ i = 0;}
            })) ;
            SK.Shutdown();
        }
    }
}
