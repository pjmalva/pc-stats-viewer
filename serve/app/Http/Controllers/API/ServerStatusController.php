<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

use App\Models\Server;
use App\Models\ServerStatus;
use App\Http\Resources\Complete\ServerStatus as ServerStatusCompleteResource;

class ServerStatusController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index(Request $request)
    {
        $search = new ServerStatus();

        if ( isset( $request->server ) ) {
            $search = $search->where('server_id', $request->server);
        }

        if ( isset( $request->interval ) ) {
            $search = $search->whereBetween('created_at', [ $request->interval[0], $request->interval[1]]);
        }

        $search = $search->orderBy('id', 'desc');

        if ( isset( $request->list ) ) {
            if ( $request->list == 0 ) {
                $items = $search->get();
            } else {
                $items = $search->paginate( $request->list );
            }
        } else {
            $items = $search->first();
        }

        return $items;
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $item = ServerStatus::findOrFail( $id );
        return $item;
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $item = ServerStatus::findOrFail( $id );
        if( $item->delete() ) {
            return $item;
        }
    }

    public function getCurrentStatus(Request $request) {
        $search = new ServerStatus();
        $search = $search->where('server_id', $request->listit);
        $search = $search->orderBy('id', 'desc');
        $items = $search->first();
        $content = json_decode( $items->content );
        return new ServerStatusCompleteResource($content);
    }

    public function updateStatus(Request $request)
    {
        $server = Server::where('cID', $request->cID)
            ->where('is_active', TRUE)
            ->firstOrFail();
        $server->last_update = date('Y-m-d H:i:s');
        $server->save();

        if ( $server->store_statuses ) {
            $server_satus = new ServerStatus();
        } else {
            $server_satus = ServerStatus::where('server_id', $server->id)->orderBy('id', 'DESC')->first();
            $server_satus = $server_satus === null ? new ServerStatus() : $server_satus;
        }

        $server_satus->server_id = $server->id;
        $server_satus->content = $request->getContent();
        $server_satus->save();

        return response()->json( $server_satus );
    }

}
