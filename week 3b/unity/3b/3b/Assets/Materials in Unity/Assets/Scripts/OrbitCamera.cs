using UnityEngine;
using System.Collections;

public class OrbitCamera : MonoBehaviour {

    [SerializeField]
    private Transform target;
    [SerializeField]
    private float rotationSpeed = 10f;
    [SerializeField, Range(0, 1)]
    private float bobSpeed = 0.2f;
    [SerializeField]
    private float bobHeight = 4f;
    [SerializeField]
    private float bobHeightVariation = 0.3f;

    private float cameraBob;

    void OnPreRender() {

        // Update the vertical camera bob
        cameraBob = Mathf.Sin(Time.time * bobSpeed) * bobHeightVariation + bobHeight;
        transform.position = new Vector3(transform.position.x, cameraBob, transform.position.z);

        // Update the camera rotation
        transform.RotateAround(target.position, Vector3.up, rotationSpeed * Time.deltaTime);

        // Update the camera look
        transform.LookAt(target);

    }

}
