using System.Collections;
using System.Collections.Generic;
using System.Net.Mime;
using System.Runtime.CompilerServices;
using UnityEngine;
using UnityEngine.UI;

public class ChangeModesScript : MonoBehaviour
{
    private Renderer renderer;
    public Text FiltermodeText;
    public Text WrapModeText;
    public Text AnisoLevelText;
  
    void Start () {
        renderer = this.gameObject.GetComponent<Renderer>();
//        renderer.material.mainTextureScale = new Vector2(1, 1);
    }
	
	void Update () {
        
//        renderer.material.SetTextureOffset();

        // filtermode
	    if (Input.GetKeyDown(KeyCode.Alpha1))
	    {
	        renderer.material.mainTexture.filterMode = 0;
	    }
        else if(Input.GetKeyDown(KeyCode.Alpha2))
	    {
	        renderer.material.mainTexture.filterMode = (FilterMode) 1;
        }
	    else if (Input.GetKeyDown(KeyCode.Alpha3))
	    {
	        renderer.material.mainTexture.filterMode = (FilterMode) 2;
	    }

        // filtermode
	    else if (Input.GetKeyDown(KeyCode.Alpha4))
	    {
	        renderer.material.mainTexture.wrapMode = 0;
	    }
	    else if (Input.GetKeyDown(KeyCode.Alpha5))
	    {
	        renderer.material.mainTexture.wrapMode = (TextureWrapMode) 1;
	    }
	    else if (Input.GetKeyDown(KeyCode.Alpha6))
	    {
	        renderer.material.mainTexture.wrapMode = (TextureWrapMode) 2;
	    }
	    else if (Input.GetKeyDown(KeyCode.Alpha7))
	    {
	        renderer.material.mainTexture.wrapMode = (TextureWrapMode) 3;
	    }
        
        // anisolevel
	    else if (Input.GetKeyDown(KeyCode.Alpha8))
	    {
	        renderer.material.mainTexture.anisoLevel -= 1;
	    }
	    else if (Input.GetKeyDown(KeyCode.Alpha9))
	    {
	        renderer.material.mainTexture.anisoLevel += 1;
	    }
        
	    FiltermodeText.text = "FilterMode : " + renderer.material.mainTexture.filterMode;
	    WrapModeText.text = "WrapMode : " + renderer.material.mainTexture.wrapMode;
	    AnisoLevelText.text = "AnisoLevel : " + renderer.material.mainTexture.anisoLevel;


    }
}
