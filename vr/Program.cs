using StereoKit;
using System;
using System.Net.Http;
using System.Text;
using Newtonsoft.Json;

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

        // method to send contoller data to API
        static void sendControls(Handed hand)
        {
            // Initialize temp variables

            // The controller specific to the hand it is in
            Controller c = Input.Controller(hand);

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


            // Create assets used by the app
            Pose cubePose = new Pose(0, 0, -0.5f, Quat.Identity);
            Model cube = Model.FromMesh(
                Mesh.GenerateRoundedCube(Vec3.One * 0.1f, 0.02f),
                Default.MaterialUI);  
    
            // Core application loop

            int i = 0;
            while (SK.Step(() =>
            {

                //only send instructions certain ammount of times per second
                if (i == 0)
                {
                    sendControls(Handed.Left);
                    sendControls(Handed.Right);
                }
                
                UI.Handle("Cube", ref cubePose, cube.Bounds);
                cube.Draw(cubePose.ToMatrix());

                i += 1;
                // make i larger or smaller depending on how many times you want the API to get posted to per second
                if (i >= 15){ i = 0;}
            })) ;
            SK.Shutdown();
        }
    }
}
